import cProfile
import logging
logging.basicConfig(level=logging.DEBUG)

from plex import Plex
from plex_metadata import Library

from shove import Shove
import argparse
import os
import time

# Build caches
cache_dir = os.path.abspath('cache')

http_cache = Shove('file://%s' % os.path.join(cache_dir, 'http'), 'memory://', optimize=False)
matcher_cache = Shove('file://%s' % os.path.join(cache_dir, 'matcher'), 'memory://', optimize=False)


def fetch_shows():
    result = {}

    for guid, shows in Library.all(types=['show']).items():
        show = shows[0]

        episodes = Library.episodes(show.rating_key, show)

        result[guid] = {
            'show': show,
            'episodes': episodes
        }

    return result


def fetch_movies():
    result = {}

    for guid, movies in Library.all(types=['movie']).items():
        movie = movies[0]

        result[guid] = {
            'movie': movie
        }

    return result


def measure(func, *args, **kwargs):
    started = time.time()

    result = func(*args, **kwargs)

    return time.time() - started, result


def test_shows():
    shows_elapsed, shows = measure(fetch_shows)

    print '-' * 50
    print '[%s] len(shows): %s' % (shows_elapsed, len(shows))
    print '-' * 50

    shows_elapsed, shows = measure(fetch_shows)

    print '-' * 50
    print '[%s] len(shows): %s' % (shows_elapsed, len(shows))
    print '-' * 50

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', action='store_true')

    args = parser.parse_args()
    pr = None

    # Setup/Enable profiling
    if args.profile:
        pr = cProfile.Profile()
        pr.enable()

    # Start test (with http + matcher caching)
    with Plex.configuration.cache(http=http_cache, matcher=matcher_cache):
        test_shows()

    # Finish profiling
    if pr:
        pr.disable()
        pr.dump_stats('library.prof')

    # Close shove caches
    http_cache.close()
    matcher_cache.close()

import logging
logging.basicConfig(level=logging.DEBUG)

from plex import Plex
from plex_metadata import Library

from shove import Shove
import argparse
import cProfile
import os
import subprocess
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
    t_elapsed = []

    for x in range(2):
        elapsed, shows = measure(fetch_shows)

        print '] %.02fs' % elapsed
        t_elapsed.append(elapsed)

    # Calculate test statistics
    t_min = min(t_elapsed)
    t_max = max(t_elapsed)
    t_avg = sum(t_elapsed) / len(t_elapsed)

    print '] min: %.02f, max: %.02f, avg: %.02f' % (t_min, t_max, t_avg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', action='store_true')
    parser.add_argument('--graph', action='store_true')
    parser.add_argument('--view', action='store_true')

    args = parser.parse_args()
    pr = None

    if args.profile:
        # Setup/Enable profiling
        pr = cProfile.Profile()
        pr.enable()

    # Start test (with http + matcher caching)
    with Plex.configuration.cache(http=http_cache, matcher=matcher_cache):
        test_shows()

    if pr and args.profile:
        # Finish profiling
        pr.disable()
        pr.dump_stats('library.prof')

        print '[PROFILE] Done'

    if pr and args.graph:
        # Convert profile to dot
        subprocess.Popen(['python', os.environ['GPROF2DOT'], '-fpstats', 'library.prof', '-olibrary.dot'])
        print '[DOT] Done'

        # Convert dot to png
        with open('library.png', 'w') as fp:
            p = subprocess.Popen(['dot', '-Tpng', 'library.dot'], stdout=fp)
            ret_code = p.wait()

        print '[PNG] Done (%s)' % ret_code

    if pr and args.graph and args.view:
        # Display image (in default viewer)
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'library.png'))
        print '[VIEW] Opening image at "%s"' % path

        os.system("start %s" % path)

    # Close shove caches
    http_cache.close()
    matcher_cache.close()

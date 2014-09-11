import logging
logging.basicConfig(level=logging.DEBUG)

from plex_metadata import Library

if __name__ == '__main__':
    show_library = Library.all(types=['show'])

    for guid, shows in show_library.items():
        show = shows[0]

        print '[%s] %s (%s)' % (guid, show.title, show)

        episodes = Library.episodes(show.rating_key, show)

        for identifier, episode in episodes.items():
            print '\t[%s] %s (%s)' % (identifier, episode.title, episode)

        break

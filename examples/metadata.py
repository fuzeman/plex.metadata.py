import logging
logging.basicConfig(level=logging.DEBUG)

from plex import Plex
from plex_activity import Activity
from plex_metadata import Guid, Matcher, Metadata
from shove import Shove

def get_item(key):
    episode = Metadata.get(3)
    print "episode:", episode

    guid = Guid.parse(episode.guid)
    print "guid:", guid

    identifier = Matcher.process(episode)
    print "identifier:", identifier


if __name__ == '__main__':
    Metadata.cache = Shove('memory://', 'memory://')
    Metadata.client = Plex.client

    get_item(3)

    Activity.start()

    while True:
        raw_input()

        get_item(3)

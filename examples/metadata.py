import logging

logging.basicConfig(level=logging.DEBUG)

from plex import Plex
from plex.objects.library.metadata.episode import Episode
from plex_activity import Activity
from plex_metadata import Guid, Matcher, Metadata
from shove import Shove

def get_item(key):
    metadata = Metadata.get(key)
    print "metadata:", metadata

    if type(metadata) is Episode:
        guid = Guid.parse(metadata.guid)
        print "guid:", guid

        identifier = Matcher.process(metadata)
        print "identifier:", identifier


if __name__ == '__main__':
    Metadata.cache = Shove('memory://', 'memory://')
    Metadata.client = Plex.client

    get_item(3)

    Activity.start()

    while True:
        raw_input()

        get_item(195)

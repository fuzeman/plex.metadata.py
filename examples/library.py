import logging
logging.basicConfig(level=logging.DEBUG)

from plex.ext.metadata import Library

if __name__ == '__main__':
    print Library.all(types=['show'])

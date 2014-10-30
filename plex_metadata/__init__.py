import logging

log = logging.getLogger(__name__)

__version__ = '0.6.0'


try:
    from plex_metadata import guid, library, matcher, metadata

    # Global objects (using defaults)
    Guid = guid.Guid
    Library = library.Library
    Matcher = matcher.Default
    Metadata = metadata.Default
except Exception, ex:
    log.warn('Unable to import submodules - %s', ex)

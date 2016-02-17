from plex_metadata.core.helpers import try_convert

import logging
import re

log = logging.getLogger(__name__)


class Agent(object):
    def __init__(self, media, service, regex=None, children=None):
        self.media = media
        self.service = service

        self.regex = regex
        self.children = children

    #
    # Compile
    #

    @classmethod
    def compile(cls, entry):
        return cls(
            media=entry.get('media'),
            service=entry.get('service'),

            # Compile regular expression
            regex=cls.compile_pattern(entry.get('pattern')),

            # Compile children
            children=[
                cls.compile(child)
                for child in (entry.get('children') or [])
            ]
        )

    @staticmethod
    def compile_pattern(pattern):
        if pattern is None:
            return None

        try:
            return re.compile(pattern, re.IGNORECASE)
        except Exception, ex:
            log.warn('Unable to compile regular expression: %r - %s', pattern, ex, exc_info=True)

        return None

    #
    # Fill
    #

    def fill(self, guid, uri, media=None):
        # Validate media matches agent
        if media is not None and media not in self.media:
            return False

        # Search children for match
        if self.children:
            # Iterate over children, checking if `guid` can be filled
            for child in self.children:
                if child.fill(guid, uri, media):
                    return True

        # Parse netloc (media id)
        if self.regex:
            # Match `uri.netloc` against pattern
            match = self.regex.match(uri.netloc)

            if not match:
                return False

            id = ''.join(match.groups())
        else:
            id = uri.netloc

        # Update `guid`
        guid.service = self.service
        guid.id = id

        # Fill `guid` with details from path (season, episode)
        self.fill_path(guid, uri.path)

        return True

    @staticmethod
    def fill_path(guid, path):
        # Split path into fragments
        fragments = path.strip('/').split('/')

        # Retrieve TV parameters
        if len(fragments) >= 1:
            guid.season = try_convert(fragments[0], int)

        if len(fragments) >= 2:
            guid.episode = try_convert(fragments[1], int)

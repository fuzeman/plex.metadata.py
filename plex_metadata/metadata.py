from plex import Plex
from plex_metadata.core.cache import Cache
from plex_metadata.core.defaults import DEFAULT_TYPES


# TODO automatic invalidated object removal (+ manual trigger)
class Metadata(object):
    def __init__(self, types=None):
        if types is not None:
            self.types = types
        else:
            self.types = DEFAULT_TYPES

        self.cache = Cache('plex.metadata')
        self.cache.on_refresh.subscribe(self.on_refresh)

        # TODO bind to activity events
        # EventManager.subscribe('notifications.timeline.created', cls.timeline_created)
        # EventManager.subscribe('notifications.timeline.deleted', cls.timeline_deleted)
        # EventManager.subscribe('notifications.timeline.finished', cls.timeline_finished)

    def get(self, key):
        return self.cache.get(key, refresh=True)

    #
    # Event handlers
    #

    def on_refresh(self, key):
        container = Plex['library'].metadata(key)

        items = list(container)

        if not items:
            log.warn('Unable to retrieve item, container empty')
            return None

        item = items[0]

        # Ignore if this is an unsupported media type
        if item.type not in self.types:
            # TODO set flag to ignore future refresh requests
            log.warn('Item %s with type "%s" has been ignored', key, item.get('type'))
            return None

        return item

    #
    # Timeline event handlers
    #

    @classmethod
    def timeline_created(cls, item):
        log.debug('timeline_created(%s)', item)

    @classmethod
    def timeline_deleted(cls, item):
        log.debug('timeline_deleted(%s)', item)

        cls.cache.remove(str(item['itemID']))

    @classmethod
    def timeline_finished(cls, item):
        log.debug('timeline_finished(%s)', item)

        cls.cache.invalidate(str(item['itemID']), refresh=True, create=True)

DEFAULT_TYPES = ['movie', 'show', 'episode']

DEFAULT_AGENT_MAP = {
    # Multi
    'mcm':              ('thetvdb', r'MCM_TV_A_(.*)'),

    # Movie
    'xbmcnfo':          'imdb',
    'standalone':       'themoviedb',

    # TV
    'abstvdb':          'thetvdb',
    'thetvdbdvdorder':  'thetvdb',
    'xbmcnfotv':        [
        ('imdb', r'(tt\d+)'),
        'thetvdb'
    ],
}

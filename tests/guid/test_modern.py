import logging
logging.basicConfig(level=logging.DEBUG)

from plex_metadata import Guid


#
# AniDb
#


def test_anidb_episode():
    guids = [
        'com.plexapp.agents.anidb://1234/1/71?lang=en',
        'com.plexapp.agents.hama://anidb-1234/1/71?lang=en'
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'anidb'
        assert r.id == '1234'

        assert r.season == 1
        assert r.episode == 71

        assert r.language == 'en'


#
# MyAnimeList
#


def test_myanimelist_episode():
    guids = [
        'net.fribbtastic.coding.plex.myanimelist://1234/1/71?lang=en'
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'myanimelist'
        assert r.id == '1234'

        assert r.season == 1
        assert r.episode == 71

        assert r.language == 'en'


#
# The TVDb
#


def test_tvdb_show():
    guids = [
        'com.plexapp.agents.thetvdb://12345?lang=en'
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'tvdb'
        assert r.id == '12345'

        assert r.season is None
        assert r.episode is None

        assert r.language == 'en'


def test_tvdb_episode():
    guids = [
        'com.plexapp.agents.abstvdb://12345/13/52?lang=en',
        'com.plexapp.agents.hama://tvdb-12345/13/52?lang=en',
        'com.plexapp.agents.thetvdb://12345/13/52?lang=en',
        'com.plexapp.agents.thetvdbdvdorder://12345/13/52?lang=en',
        'com.plexapp.agents.xbmcnfotv://12345/13/52?lang=en',
        'com.plexapp.agents.mcm://MCM_TV_A_12345/13/52?lang=en'
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'tvdb'
        assert r.id == '12345'

        assert r.season == 13
        assert r.episode == 52

        assert r.language == 'en'


#
# IMDb
#


def test_imdb_movie():
    guids = [
        'com.plexapp.agents.imdb://tt12345',
        'com.plexapp.agents.xbmcnfotv://tt12345'
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'imdb'
        assert r.id == 'tt12345'

        assert r.language is None


def test_imdb_episode():
    guids = [
        'com.plexapp.agents.hama://imdb-12345/1/71?lang=en'
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'imdb'
        assert r.id == '12345'

        assert r.season == 1
        assert r.episode == 71

        assert r.language == 'en'


#
# The Movie Database
#


def test_tmdb_movie():
    guids = [
        'com.plexapp.agents.standalone://12345',
        'com.plexapp.agents.themoviedb://12345'
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'tmdb'
        assert r.id == '12345'

        assert r.language is None


def test_tmdb_episode():
    guids = [
        'com.plexapp.agents.themoviedb://12345/3/2?lang=en',
        'com.plexapp.agents.hama://tmdb-12345/3/2?lang=en'
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'tmdb'
        assert r.id == '12345'

        assert r.season == 3
        assert r.episode == 2

        assert r.language == 'en'


#
# Misc
#


def test_media():
    guids = [
        'com.plexapp.agents.thetvdb://12345'
    ]

    for item in guids:
        r = Guid.parse(item, media='movie')

        assert r is None


def test_no_match():
    guids = [
        'com.plexapp.basic://12345/3/2?lang=en'
    ]

    for item in guids:
        r = Guid.parse(item, match=False)

        assert r.service == 'basic'
        assert r.id == '12345'


def test_unsupported():
    guids = [
        'com.plexapp.unsupported://12345/3/2?lang=en',
        'com.plexapp.unsupported://',
        '://12345',
        None
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r is None

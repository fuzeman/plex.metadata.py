import logging
logging.basicConfig(level=logging.DEBUG)

from plex_metadata import Guid


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


def test_tvdb_episode():
    guids = [
        'com.plexapp.agents.abstvdb://12345/13/52?lang=en',
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


def test_tmdb_episode():
    guids = [
        'com.plexapp.agents.themoviedb://12345/3/2',
    ]

    for item in guids:
        r = Guid.parse(item)

        assert r.service == 'tmdb'
        assert r.id == '12345'

        assert r.season == 3
        assert r.episode == 2

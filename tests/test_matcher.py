import logging
logging.basicConfig(level=logging.DEBUG)

from plex_metadata import Matcher


def test_parse():
    cases = [
        ('Show.Name.S05E10-11', [{'season': '05', 'episode_from': '10', 'episode_to': '11'}]),
        ('Show.Name.S05E10E11', [{'season': '05', 'episode': ['10', '11']}]),
        ('Show.Name.5x13', [{'season': '5', 'episode': '13'}])
    ]

    for file_name, expected in cases:
        assert Matcher.parse(file_name) == expected

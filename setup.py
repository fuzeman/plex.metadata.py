from plex_metadata import __version__

from setuptools import setup

setup(
    name='plex.metadata.py',
    version=__version__,
    license='MIT',
    url='https://github.com/fuzeman/plex.metadata.py',

    author='Dean Gardiner',
    author_email='me@dgardiner.net',

    description='Metadata extension for plex.py',
    packages=['plex_metadata'],
    platforms='any',

    install_requires=[
        'plex.py',
        'plex.activity.py'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)

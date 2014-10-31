from plex_metadata import __version__

from setuptools import setup, find_packages

setup(
    name='plex.metadata.py',
    version=__version__,
    license='MIT',
    url='https://github.com/fuzeman/plex.metadata.py',

    author='Dean Gardiner',
    author_email='me@dgardiner.net',

    description='Metadata extension for plex.py',
    packages=find_packages(exclude=['tests']),
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

0.6.1 (2015-02-05)
------------------
**Changes**
 - Setup travis-ci testing and coverage (via coveralls)
 - [library] display a warning when :code:`Library.item_map()` fails due to a invalid/missing "guid" property
 - [library] exclude sections without an agent
 - [metadata] automatically invalidate media with invalid/missing "guid" properties
 - [tests] added unit tests for :code:`plex_metadata.guid` and :code:`plex_metadata.matcher`

**Fixed**
 - Python 3.x compatibility issues
 - [guid] parsing bug on Python 2.6
 - [guid] :code:`Guid.map_guid()` could return an invalid return type in some cases
 - [library] possible case where :code:`Guid.parse()` returns :code:`None`
 - [library] handle a case where :code:`Metadata.get()` returns :code:`None`
 - [matcher] catch an error where episodes have no "media" or "parts"
 - [matcher] handle a case where :code:`Caper.parse()` returns :code:`None`
 - [metadata] catch metadata request failures

0.6.0 (2014-10-30)
------------------
- Initial release
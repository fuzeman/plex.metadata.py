0.7.1 (2016-02-12)
------------------
**Changed**
 - Reduced severity of `Item ... with type "..." has been ignored` message
 - Updated travis configuration (python: dropped 3.2, added 3.4 and 3.5)

**Fixed**
 - Episode range size is now limited in the matcher to avoid cpu/memory exhaustion

0.7.0 (2015-09-12)
------------------
**Added**
 - [guid] :code:`Guid.__repr__()` and :code:`Guid.__str__()` methods
 - [matcher] :code:`Matcher.set_caper()` and :code:`Matcher.set_extend()` methods

**Changed**
 - [library] :code:`Library.episodes()` now prefers real :code:`Episode` objects over multi-episode duplicates
 - [library] Return :code:`None` from :code:`Library.all()` if the request fails
 - [metadata] only cache metadata with a valid guid
 - [metadata] cache unsupported items as :code:`False` to avoid refreshing on every request
 - [metadata] return :code:`False` on unsupported media

**Fixed**
 - Issue handling invalid guids

0.6.1 (2015-02-05)
------------------
**Changed**
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
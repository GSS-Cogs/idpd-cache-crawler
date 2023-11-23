# TODO - you'll need a logger, dont worry about structured logs at this point
# (as we'll want a generic one that all the apps use) but come up with something
# that'll support the basic patterns of:
#
# logger.debug("message", data={"some": "field"})
# and
# logger.error("message", data={"other": "field", error=[Python Exception]})
#
# As long as it will accept those signatures that's enough for now, we can nuance
# the logger later that way without having to change any logging statements you
# add to the wider app.
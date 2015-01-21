import slask
from nose.tools import eq_

#TODO:
# * configurable logging.
# * test log messages.

def test_plugin_success():
    hooks = slask.init_plugins("test/plugins")
    eq_( len(hooks) ,  1)
    assert "message" in hooks
    assert isinstance(hooks, dict)
    assert isinstance(hooks["message"], list)
    eq_( len(hooks["message"]) ,  1)
    eq_( hooks["message"][0]({"text": u"bananas"}, None) ,  u"bananas")

def test_plugin_invalid_dir():
    hooks = slask.init_plugins("invalid/package")
    eq_( len(hooks) ,  0)

def test_run_hook():
    hooks = slask.init_plugins("test/plugins")
    eq_(slask.run_hook(hooks, "message", {"text": u"bananas"}, None), [u"bananas"])

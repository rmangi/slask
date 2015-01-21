import slask

#TODO:
# * configurable logging.
# * test log messages.

def test_plugin_success():
    hooks = slask.init_plugins("test/plugins")
    assert len(hooks) == 1
    assert "message" in hooks
    assert isinstance(hooks, dict)
    assert isinstance(hooks["message"], list)
    assert len(hooks["message"]) == 1
    assert hooks["message"][0]({"text": "bananas"}, None) == "bananas"

def test_plugin_invalid_dir():
    hooks = slask.init_plugins("invalid/package")
    assert len(hooks) == 0

import slask

def test_run():
    hooks = slask.init_plugins("test/plugins")
    print hooks

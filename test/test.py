import sys
sys.path.insert(0, "..")

import slask

def test_run():
    slask.init_plugins()
    print slask.hooks

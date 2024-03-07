import pytest
from ukp_project_template import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from ukp_project_template import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####

##########################
"""
Pytest shouldn't be able to collect this file automatically with discovery because it lacks
the naming conventions for discovery
"""

def test_simple():
    assert True

def test_fails():
    assert False
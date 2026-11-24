import importlib.util


def test_greet_says_hello():
    assert importlib.util.find_spec("hello") is not None, "hello.py is missing"
    from hello import greet
    assert greet() == "hello"

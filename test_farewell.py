import hello


def test_farewell_says_goodbye():
    assert getattr(hello, "farewell", None) is not None, "farewell() is missing"
    assert hello.farewell() == "goodbye"

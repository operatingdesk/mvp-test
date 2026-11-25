import hello


def test_welcome_greets_by_name():
    assert getattr(hello, "welcome", None) is not None, "welcome() is missing"
    assert hello.welcome("Ada") == "hello, Ada"

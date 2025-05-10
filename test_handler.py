import handler


def test_handler():
    assert handler.handler(None, None) == "Hello, CodeBuild!"

# project/tests/test_ping.py

from app import main


def test_ping(test_app):
    # Given
    # test_app

    # When
    response = test_app.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}

# if a class is used, it must begin with Test
class TestFoo:

    # test functions must begin with test_
    def test_bar(self):
        assert "foo" != "bar"

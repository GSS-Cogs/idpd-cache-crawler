import pytest 
import os

from crawlers.base import _get_headers

def test_get_headers_without_env_vars():
    headers = _get_headers()

    assert type(headers) == dict

    for key, value in headers:
        assert type(key) == str
        assert type(value) == str
        assert "," not in key
        assert "=" not in key
        assert "," not in value
        assert "=" not in value

    assert headers.get("Cache-Control") is not None
    assert headers.get("Cache-Control") == "no-cache"
    assert headers.get("Pragma") is not None
    assert headers.get("Pragma") == "no-cache"


def test_get_headers_with_env_vars():
    os.environ['ADDITIONAL_HEADERS'] = 'user=username,password=1234'
    headers = _get_headers()

    assert type(headers) == dict

    for key, value in headers:
        assert type(key) == str
        assert type(value) == str
        assert "," not in key
        assert "=" not in key
        assert "," not in value
        assert "=" not in value
    
    assert headers.get("Cache-Control") is not None
    assert headers.get("Cache-Control") == "no-cache"
    assert headers.get("Pragma") is not None
    assert headers.get("Pragma") == "no-cache"
    assert headers.get("user") is not None
    assert headers.get("user") == "username"
    assert headers.get("password") is not None
    assert headers.get("password") == "1234"


def test_get_headers_raises_exception_about_additional_headers():
    with pytest.raises(Exception) as excinfo:
        os.environ['ADDITIONAL_HEADERS'] = 1432
        headers = _get_headers()

        assert "ADDITIONAL_HEADERS doesn't conatin str like value" in excinfo


def test_get_headers_raises_about_headers():
    with pytest.raises(Exception) as excinfo:
        os.environ['ADDITIONAL_HEADERS'] = 'singleWordWithNoKeyOrValue'
        headers = _get_headers()

        assert "Some HEADERS in ADDITIONAL_HEADERS are not key value pairs" in excinfo
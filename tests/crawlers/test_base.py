import pytest 
import os

from src.crawlers.base import _get_headers


def test_get_headers_returns_valid_dict_without_env_vars():
    """
    testing _get_headers() returns a dict containing 
    cache control no cache
    """
    headers = _get_headers()

    assert type(headers) == dict

    for key, value in headers.items():
        assert type(key) == str
        assert type(value) == str
        assert "," not in key
        assert "=" not in key
        assert "," not in value
        assert "=" not in value

    assert headers.get("Cache-Control") == "no-cache"
    assert headers.get("Pragma") == "no-cache"


def test_get_headers_returns_valid_dict_with_env_vars():
    """
    testing _get_headers() returns a dict containing 
    cache control no cache, as well as the additional headers
    defined in the env vars
    """
    os.environ['ADDITIONAL_HEADERS'] = 'user=username,password=1234'
    headers = _get_headers()

    assert type(headers) == dict

    for key, value in headers.items():
        assert type(key) == str
        assert type(value) == str
        assert "," not in key
        assert "=" not in key
        assert "," not in value
        assert "=" not in value
    
    assert headers.get("Cache-Control") == "no-cache"
    assert headers.get("Pragma") == "no-cache"
    assert headers.get("user") == "username"
    assert headers.get("password") == "1234"


def test_get_headers_returns_valid_dict_when_env_var_has_white_spaces():
    """
    testing _get_headers() returns a dict containing 
    cache control no cache and additional headers, 
    when the env vars contain white spaces
    and duplicate white spaces
    """
    with pytest.raises(Exception) as excinfo:
        os.environ['ADDITIONAL_HEADERS'] = 'single Word  With No   Key Or Value'
        _get_headers()

    assert ("Some HEADERS in ADDITIONAL_HEADERS are not key value pairs" in str(excinfo.value))


# def test_get_headers_raises_exception_about_additional_headers():
#     """
#     Testing to see if exception is raised when the env vars conatin 
#     data types other than a string
#     """
#     with pytest.raises(Exception) as excinfo:
#         os.environ['ADDITIONAL_HEADERS'] = int(1432)
#         _get_headers()

#     assert ("ADDITIONAL_HEADERS doesn't conatin str like value" in str(excinfo.value))


def test_get_headers_raises_about_headers():
    """
    Testing to see if an exception is raised after ADDITIONAL_HEADERS
    is split into HEADERS, to see if each header is missing an '=' in them
    to signify no key and value, where each header should take the form of '{key}={value}'
    """
    with pytest.raises(Exception) as excinfo:
        os.environ['ADDITIONAL_HEADERS'] = 'singleWordWithNoKeyOrValue'
        _get_headers()

    assert ("Some HEADERS in ADDITIONAL_HEADERS are not key value pairs" in str(excinfo.value))


def test_get_headers_raises_about_headers_containing_malformed_entries():
    """
    Testing to see if each 'header in HEADERS' don't have 
    malformed entry, eg: key=value=typo or key==value
    """
    with pytest.raises(Exception) as excinfo:
        os.environ['ADDITIONAL_HEADERS'] = 'single==Word=With==No=Key=Or=Value'
        _get_headers()

    assert ("Malformed entry, eg: key=value=typo or key==value" in str(excinfo.value))
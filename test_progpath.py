import platform
from pathlib import Path

import pytest

from progpath import (
    UnsupportedPlatformError,
    user_cache_path,
    user_config_path,
    user_data_path,
)


def test_user_data_path():
    path = user_data_path()
    assert isinstance(path, Path)
    path = user_data_path("test")
    assert isinstance(path, Path)


def test_user_cache_path():
    path = user_cache_path()
    assert isinstance(path, Path)
    path = user_cache_path("test")
    assert isinstance(path, Path)


def test_user_config_path():
    path = user_config_path()
    assert isinstance(path, Path)
    path = user_config_path("test")
    assert isinstance(path, Path)


def test_unsupported_platform():
    original_system = platform.system
    try:
        platform.system = lambda: "Unsupported"
        with pytest.raises(UnsupportedPlatformError):
            user_data_path()
    finally:
        platform.system = original_system

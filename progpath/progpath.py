import os
import platform
from pathlib import Path
from typing import Optional


class UnsupportedPlatformError(Exception):
    pass


def user_data_path(prog: Optional[str] = None) -> Path:
    match platform.system():
        case "Windows":
            path = Path(os.getenv("LOCALAPPDATA"))
        case "Linux":
            path = Path(
                os.getenv("XDG_DATA_HOME", "~/.local/share")
            ).expanduser()
        case "Darwin":
            path = Path("~/Library/Application Support").expanduser()
        case _:
            raise UnsupportedPlatformError
    if not prog:
        return path
    return path.joinpath(prog)


def user_config_path(prog: Optional[str] = None) -> Path:
    match platform.system():
        case "Windows":
            path = Path(os.getenv("LOCALAPPDATA"))
            if prog:
                return path.joinpath(prog, Path("config"))
        case "Linux":
            path = Path(os.getenv("XDG_CONFIG_HOME", "~/.config")).expanduser()
        case "Darwin":
            path = Path("~/Library/Preferences").expanduser()
        case _:
            raise UnsupportedPlatformError
    if not prog:
        return path
    return path.joinpath(prog)


def user_cache_path(prog: Optional[str] = None) -> Path:
    match platform.system():
        case "Windows":
            path = Path(os.getenv("LOCALAPPDATA"))
            if prog:
                return path.joinpath(prog, "cache")
        case "Linux":
            path = Path(os.getenv("XDG_CACHE_HOME", "~/.cache")).expanduser()
        case "Darwin":
            path = Path("~/Library/Caches").expanduser()
        case _:
            raise UnsupportedPlatformError
    if not prog:
        return path
    return path.joinpath(prog)


print(user_cache_path())
print(user_config_path())
print(user_data_path())
print(user_cache_path("balls"))
print(user_config_path("balls"))
print(user_data_path("balls"))

from importlib.metadata import PackageNotFoundError, version

from progpath.progpath import *  # noqa: F403

try:
    __version__ = version(__package__)
except PackageNotFoundError:
    __version__ = "0.0.0"

# progpath

[![License](https://img.shields.io/github/license/st0rmw1ndz/progpath)](https://github.com/st0rmw1ndz/progpath/blob/main/LICENSE)
[![GitHub tag](https://img.shields.io/github/v/tag/st0rmw1ndz/progpath)](https://github.com/st0rmw1ndz/progpath/releases)
[![Actions status](https://github.com/st0rmw1ndz/progpath/workflows/CI/badge.svg)](https://github.com/st0rmw1ndz/progpath/actions)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A convenient way to store your program's data.

## Example Usage

### Windows

```python
>>> import progpath

>>> name = "EpicApp"

>>> progpath.user_data_path(name)
WindowsPath('C:/Users/frosty/AppData/Local/EpicApp')

>>> progpath.user_config_path(name)
WindowsPath('C:/Users/frosty/AppData/Local/EpicApp/config')

>>> progpath.user_cache_path(name)
WindowsPath('C:/Users/frosty/AppData/Local/EpicApp/cache')
```

### Linux

```python
>>> import progpath

>>> name = "EpicApp"

>>> progpath.user_data_path(name)
PosixPath('/home/frosty/.local/share/EpicApp')

>>> progpath.user_config_path(name)
PosixPath('/home/frosty/.config/EpicApp')

>>> progpath.user_cache_path(name)
PosixPath('/home/frosty/.cache/EpicApp')
```

### macOS

Should be supported, but no testing has been done yet.

## Installation

```
pip install git+https://github.com/st0rmw1ndz/progpath.git
```
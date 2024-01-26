# progpath

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
pip install git+https://gitub.com/st0rmw1ndz/progpath.git
```
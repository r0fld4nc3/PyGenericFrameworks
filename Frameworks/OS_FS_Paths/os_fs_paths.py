import os
import pathlib
import platform

Path = pathlib.Path

_windows = "windows"
_linux = "linux"
_unix = "unix"
_darwin = "darwin"
_mac = "mac"
_SYSTEM = platform.system().lower()


def win_get_appdata() -> Path:
    if _windows in _SYSTEM:
        return Path(os.getenv("appdata"))
    else:
        return unix_get_share_folder()


def win_get_localappdata() -> Path:
    if _windows in _SYSTEM:
        return Path(os.getenv("localappdata"))
    else:
        return unix_get_share_folder()


def win_get_documents_folder() -> Path:
    if _windows in _SYSTEM:
        return get_home_folder() / "Documents"
    else:
        return unix_get_share_folder()


def unix_get_share_folder() -> Path:
    if _windows not in _SYSTEM:
        return get_home_folder() / ".local/share"
    else:
        return win_get_localappdata()


def get_home_folder() -> Path:
    return Path(os.path.expanduser('~'))


def get_os_env_config_folder() -> Path:
    if _windows in _SYSTEM:
        print("Target System Windows")
        _config_folder = win_get_localappdata()
    elif _linux in _SYSTEM or _unix in _SYSTEM:
        print("Target System Linux/Unix")
        _config_folder = unix_get_share_folder()
    elif _darwin in _SYSTEM or _mac in _SYSTEM:
        print("Target System MacOS")
        # Write to user-writable locations, like ~/.local/share
        _config_folder = unix_get_share_folder()
    else:
        print("Target System Other")
        print(_SYSTEM)
        _config_folder = Path.cwd()

    print(f"Config folder: {_config_folder}")

    return _config_folder
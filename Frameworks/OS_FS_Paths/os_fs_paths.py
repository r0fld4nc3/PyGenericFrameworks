import os
from pathlib import Path
import platform

_windows = "windows"
_linux = "linux"
_unix = "unix"
_darwin = "darwin"
_mac = "mac"


def win_get_appdata() -> Path:
    if _windows in system():
        return Path(os.getenv("appdata"))
    else:
        return unix_get_share_folder()


def win_get_localappdata() -> Path:
    if _windows in system():
        return Path(os.getenv("localappdata"))
    else:
        return unix_get_share_folder()


def win_get_documents_folder() -> Path:
    if _windows in system():
        return get_home_folder() / "Documents"
    else:
        return unix_get_share_folder()


def unix_get_share_folder() -> Path:
    if _windows not in system():
        return unix_get_local_folder() / "share"
    else:
        return win_get_localappdata()


def unix_get_local_folder() -> Path:
    if _windows not in system():
        return get_home_folder() / ".local"
    else:
        return win_get_localappdata()

def unix_get_config_folder() -> Path:
    if _windows not in system():
        return get_home_folder() / ".config"
    else:
        return win_get_localappdata()


def get_home_folder() -> Path:
    return Path(os.path.expanduser('~'))


def get_env_tempdir() -> Path:
    if "windows" in system():
        _tempdir = win_get_localappdata() / "Temp"
    else:
        _tempdir = unix_get_share_folder() / "temp"

    # Ensure path exists
    ensure_paths(_tempdir)

    return _tempdir


def get_os_env_config_folder() -> Path:
    if _windows in system():
        print("Target System Windows")
        _config_folder = win_get_localappdata()
    elif _linux in system() or _unix in system():
        print("Target System Linux/Unix")
        _config_folder = unix_get_share_folder()
    elif _darwin in system() or _mac in system():
        print("Target System MacOS")
        # Write to user-writable locations, like ~/.local/share
        _config_folder = unix_get_share_folder()
    else:
        print("Target System Other")
        print(system())
        _config_folder = Path.cwd()

    ensure_paths(_config_folder)
    print(f"Config folder: {_config_folder}")

    return _config_folder


def ensure_paths(to_path: Path):
    if isinstance(to_path, Path):
        if not to_path.exists():
            if to_path.suffix:
                # It's a file
                os.makedirs(to_path.parent, exist_ok=True)
                with open(to_path, 'w') as f:
                    if to_path.suffix == ".json":
                        f.write('{}')
                    else:
                        f.write('')
            else:
                # It's a directory
                os.makedirs(to_path, exist_ok=True)
    elif isinstance(to_path, str):
        if not os.path.exists(to_path):
            if str(to_path).rpartition('.')[-1]:
                # We have a file
                os.makedirs(to_path.rpartition('.')[0])
                with open(to_path, 'w') as f:
                    if to_path.endswith(".json") == ".json":
                        f.write('{}')
                    else:
                        f.write('')
            else:
                os.makedirs(to_path)

    return Path(to_path)


def system() -> str:
    return platform.system().lower()

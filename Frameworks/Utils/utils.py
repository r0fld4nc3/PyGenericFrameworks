import os
import shutil
import stat
import time
import contextlib
from typing import Generator
from pathlib import Path
from subprocess import check_output, CalledProcessError, STDOUT


def rmtree_on_error(func, path, exc_info):
    # https://stackoverflow.com/a/2656405
    """
        Error handler for ``shutil.rmtree``.

        If the error is due to an access error (read only file)
        it attempts to add write permission and then retries.

        If the error is for another reason it re-raises the error.

        Usage : ``shutil.rmtree(path, onerror=onerror)``
        """
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise


@contextlib.contextmanager
def timing_ctx(name: str=None) -> Generator[None, None, None]:
    t0 = time.monotonic()
    try:
        yield
    finally:
        t1 = time.monotonic()
        print(f"{name} took: {round(t1 - t0, 3)}s")


def win_msgbox(text, title, style=0):
    import ctypes  # An included library with Python install.
    import ctypes.wintypes as wintypes

    #  Styles:
    #  0 : OK
    #  1 : OK | Cancel
    #  2 : Abort | Retry | Ignore
    #  3 : Yes | No | Cancel
    #  4 : Yes | No
    #  5 : Retry | Cancel
    #  6 : Cancel | Try Again | Continue

    dll = ctypes.WinDLL('user32', use_last_error=True)
    dll.MessageBoxW.argtypes = wintypes.HWND, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.UINT
    dll.MessageBoxW.restype = ctypes.c_int

    MB_SYSTEMMODAL = 0x00001000

    if style not in list(range(0, 7)):
        style = 0

    dll.MessageBoxW(0, text, title, MB_SYSTEMMODAL)


def win_show_console():
    import ctypes
    # Get the window handle of the console window
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    hwnd = kernel32.GetConsoleWindow()
    if hwnd != 0:
        # Show the console window
        user32.ShowWindow(hwnd, 1)
    else:
        # Attach a console to the current process if it doesn't exist
        kernel32.AllocConsole()


def win_hide_console():
    import ctypes
    # Get the window handle of the console window
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    hwnd = kernel32.GetConsoleWindow()
    if hwnd != 0:
        # Hide the console window
        user32.ShowWindow(hwnd, 0)
    else:
        # Detach the console from the current process if it doesn't exist
        kernel32.FreeConsole()


def delete_files_from_disk(files_list: list):
    print(f"Delete files from disk {files_list}")
    for item in files_list:
        item = Path(item)
        if item.exists():
            if item.is_file():
                print(f"[FILE] Removing {item}")
                os.remove(item)
            else:
                print(f"[DIR] Removing {item}")
                try:
                    shutil.rmtree(item, onerror=rmtree_on_error)
                except Exception as e:
                    print(e)
        else:
            print(f"File does not exist: {item}")


def run_command(command: list) -> tuple:
    """
    params:
        command: list of strings, ex. `["ls", "-l"]`
    :returns: output, success
    """
    print(f"Running command {command}")
    try:
        output = check_output(command, stderr=STDOUT).decode()
        success = True
        print(f"Output: {output}")
    except CalledProcessError as e:
        output = e.output.decode()
        print(f"{e}\n{e.output.decode()}")
        success = False
    return output, success

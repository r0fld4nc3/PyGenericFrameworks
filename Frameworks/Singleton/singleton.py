from threading import Lock

class Singleton(type):
    """
    A custom implementation of a Singleton class, aimed at being derived from.

    This base class shouldn't be edited unless excplicitly needed, however the intent is to have another
    class derive from it, such as

    from PySingleton import Singleton

    `class YourClass(Singleton):`
    """

    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]

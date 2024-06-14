# Singleton
A simple implementation of a Singleton class meant to be derived from

---

In the other modules, you can simply import it like this example
```
from source_folder.utils_singleton import Singleton
```
And use it as a metaclass (**Python3.6+**) for wichever class you want to be a Singleton
```
class MyUniqueClass(metaclass=Singleton):
```

# Context Decorators

An extremely easy way to create and implement Decorators with the added bonus of being Context Managers.

You will see `TODO` comments sprinkled around. These are guides to help with the setup process so you know what needs to be altered.

Notice it comes with `print` statements by default. You may or should replace them with a logger, so it's useful to pair with the Logger module.

Create as many Decorators as needed following the example of `example_timing_ctx`

---


In the other modules, you can simply import it like this example
```
from source_folder.utils.decorators import example_timing_ctx
```
And use it to decorate a function like so:
```
if __name__ == "__main__":
    import random

    @example_timing_ctx()
    def example_loop():
        for _ in range(5):
            time.sleep(random.random())

    example_loop()
```
Note that the deocrator can take a name, specific by each implementation of course.

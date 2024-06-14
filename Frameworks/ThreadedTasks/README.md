# Threaded Queue

An implementation of a Threaded/Queue system for parallel thread-safe task run. Useful for example, for GUI's.

You will see `TODO` comments sprinkled around. These are guides to help with the setup process so you know what needs to be altered.

## Edit the ThreadedQueue class to suit your needs

`ThreadedQueue` comes with `print` statements by default. You may or should replace them with a logger, so it's useful to pair with the Logger module.

---


In the other modules, you can simply import it like this example
```
from source_folder.utils import ThreadedQueue
```
And define it where you need to
```
task_queue = ThreadedQueue()
task_queue.start_workers()
```

To add a task:
```
task_queue.add_task(my_task_function)
```
`add_task` takes 3 parameters:
- Function name/reference
- *args
- **kwargs

When a task is added, it will start immediately as soon as the queue is free to do so, and this also depends on the number of workers that have been initialised.

You should run the function to stop work as your programme ends or you don't need the queue anymore, to prevent hanging threads and instability:
```
task_queue.stop_workers()
```

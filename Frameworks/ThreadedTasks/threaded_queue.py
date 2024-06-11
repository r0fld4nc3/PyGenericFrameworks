import queue
import threading

# TODO: Import logger here
# TODO: Optional: Import global configs

# TODO: Create/Assign Logger here
# TODO: Replace print() calls with logger calls

class ThreadedQueue:
    def __init__(self, num_workers: int=2):
        self._task_queue: queue = queue.Queue()
        self._results_queue = queue.Queue()
        if num_workers < 1:
            num_workers = 2
        self._num_workers: int = num_workers
        self._workers: list = []
        self._total_jobs = 0
        self._stopped = True

        print(f"Init with {self._workers} workers")

    @property
    def task_queue(self):
        return self._task_queue

    @property
    def results_queue(self):
        return self._results_queue

    @property
    def num_workers(self):
        return self._num_workers

    @num_workers.setter
    def num_workers(self, num: int):
        if num > 0:
            self._num_workers = num
        else:
            self._num_workers = 2

    @property
    def workers(self):
        return self._workers

    @property
    def jobs(self):
        return self._total_jobs

    def start_workers(self):
        print("Starting workers")

        self._stopped = False
        for _ in range(self._num_workers):
            print(f"threading.Thread(target={self.worker_function})")
            worker = threading.Thread(target=self.worker_function)
            worker.start()
            print(f"self.workers.append({worker})")
            self._workers.append(worker)

    def worker_function(self):
        while not self._stopped:
            print("Checking for tasks")

            # Blocks until a task becomes available
            task = self._task_queue.get()

            if isinstance(task, tuple):
                func, args, kwargs = task
                try:
                    result = func(*args, **kwargs)
                    if result is None:
                        result = False
                    self._task_queue.task_done()
                except Exception as e:
                    if e is None:
                        print(f"{e}\n {' ' * 45}{'^' * len(str(e))}")
                    result = e
                self._task_queue.put(result)
                self._results_queue.put(result)
            elif task is None:
                # Exit gracefully
                self._task_queue.task_done()
            else:
                print(f"Task of else: {task}")

    def add_task(self, func, *args, **kwargs):
        print(f"Adding task: {func}, {args}, {kwargs}")
        self._task_queue.put((func, args, kwargs))
        self._total_jobs += 1

    def stop_workers(self):
        print(f"Stopping workers ({self._num_workers})")

        self._stopped = True

        for _ in range(self._num_workers):
            print("Stopping")
            self.add_task(None)

    def empty(self) -> bool:
        return self._task_queue.qsize() == 0

    def task_queue_size(self) -> int:
        return self._task_queue.qsize()

    def results_queue_size(self) -> int:
        return self._results_queue.qsize()

    def jobs_finished(self) -> bool:
        return self.empty() and self.results_queue_size() == self._total_jobs

    def restart_counts(self):
        self._task_queue: queue = queue.Queue()
        self._results_queue = queue.Queue()
        self._workers: list = []
        self._total_jobs = 0

# Simulation of a high-performance concurrent task scheduler
import threading
import queue
import time

class TaskScheduler:
    def __init__(self, num_workers):
        self.queue = queue.Queue()
        self.workers = [threading.Thread(target=self._worker) for _ in range(num_workers)]
        for w in self.workers: w.start()

    def _worker(self):
        while True:
            task = self.queue.get()
            if task is None: break
            print(f"Executing storage task: {task}")
            time.sleep(0.1)

if __name__ == "__main__":
    scheduler = TaskScheduler(4)
    for i in range(10): scheduler.queue.put(f"data_block_{i}")
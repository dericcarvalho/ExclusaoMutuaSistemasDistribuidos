import threading

class LamportClock:
    def __init__(self):
        self.clock = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.clock += 1

    def get_time(self):
        with self.lock:
            return self.clock
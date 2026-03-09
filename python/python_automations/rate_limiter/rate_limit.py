
import time
from collections import deque

class RateLimiter(object):
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.requests = deque()

    def allow_request(self):
        current_time = time.time()
        while self.requests and current_time - self.requests[0] > self.window:
            self.requests.popleft()

        if len(self.requests) < self.limit:
            self.requests.append(current_time)
            return True

        return False

def main():
    rate_limiter = RateLimiter(5, 10)
    for i in range(100):
        if rate_limiter.allow_request():
            print("Allowed, ", i)
        else:
            print("Rate Limited, ", i)
        
        time.sleep(1)


if __name__ == '__main__':
    main()

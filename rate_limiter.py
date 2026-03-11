from collections import deque


class RateLimiter:

    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.user_requests = {}

    def allow_request(self, user, timestamp):

        if user not in self.user_requests:
            self.user_requests[user] = deque()

        requests = self.user_requests[user]

        # Remove expired timestamps
        while requests and timestamp - requests[0] > self.window:
            requests.popleft()

        if len(requests) < self.limit:
            requests.append(timestamp)
            return True, len(requests)

        return False, len(requests)
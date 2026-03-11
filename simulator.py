import time
import datetime

from rate_limiter import RateLimiter
from request_parser import parse_request
from config import RATE_LIMIT, TIME_WINDOW


def run_simulation():

    limiter = RateLimiter(RATE_LIMIT, TIME_WINDOW)

    print("Rate Limiter Simulator")
    print("Enter a user name to simulate a request")
    print("Type 'exit' to stop\n")

    while True:

        line = input("> ")

        if line.lower() == "exit":
            print("Stopping simulation...")
            break

        try:

            user = parse_request(line)

            timestamp = int(time.time())

            allowed, count = limiter.allow_request(user, timestamp)

            current_time = datetime.datetime.now().strftime("%H:%M:%S")

            if allowed:
                print(f"[{current_time}] Request from {user} → ALLOWED ({count}/{RATE_LIMIT})")
            else:
                print(f"[{current_time}] Request from {user} → BLOCKED (limit reached)")

        except ValueError as e:
            print("ERROR:", e)
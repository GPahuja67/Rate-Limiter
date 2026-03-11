import time
import datetime

from rate_limiter import RateLimiter
from request_parser import parse_request
from config import RATE_LIMIT, TIME_WINDOW


def run_simulation():

    limiter = RateLimiter(RATE_LIMIT, TIME_WINDOW)

    log_file = open("requests.log", "a")

    print("Rate Limiter Simulator")
    print("Commands:")
    print("  <username> → simulate request")
    print("  stats      → show active users")
    print("  config     → show rate limit settings")
    print("  reset      → clear all request data")
    print("  exit       → stop program\n")

    while True:

        line = input("> ").strip()

        if line.lower() == "exit":
            print("Stopping simulation...")
            break

        if line.lower() == "stats":
            print(f"Active users being tracked: {len(limiter.user_requests)}")
            continue

        if line.lower() == "config":
            print(f"Rate Limit: {RATE_LIMIT} requests")
            print(f"Time Window: {TIME_WINDOW} seconds")
            continue

        if line.lower() == "reset":
            limiter.user_requests.clear()
            print("All rate limit data cleared.")
            continue

        try:

            user = parse_request(line)

            timestamp = int(time.time())

            allowed, count = limiter.allow_request(user, timestamp)

            current_time = datetime.datetime.now().strftime("%H:%M:%S")

            if allowed:
                remaining = RATE_LIMIT - count
                message = f"[{current_time}] Request from {user} → ALLOWED ({count}/{RATE_LIMIT}) | Remaining: {remaining}"
            else:
                message = f"[{current_time}] Request from {user} → BLOCKED (limit reached)"

            print(message)

            log_file.write(f"{current_time} {user} {allowed}\n")
            log_file.flush()

        except ValueError as e:
            print("ERROR:", e)
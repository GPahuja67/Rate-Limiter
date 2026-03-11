import time
import datetime

from rate_limiter import RateLimiter
from request_parser import parse_request
from config import RATE_LIMIT, TIME_WINDOW


def run_simulation():

    limiter = RateLimiter(RATE_LIMIT, TIME_WINDOW)

    log_file = open("requests.log", "a")

    print("\n=== API Rate Limiter Simulation ===")
    print("Available Commands:")
    print("  <username> : simulate an incoming request")
    print("  stats      : display number of active users being tracked")
    print("  config     : display current rate limiting configuration")
    print("  reset      : clear all stored request data")
    print("  exit       : terminate the simulation\n")

    while True:

        line = input("> ").strip()

        if line.lower() == "exit":
            print("Shutting down the simulation...")
            break

        if line.lower() == "stats":
            print(f"System Status: Tracking {len(limiter.user_requests)} active user(s).")
            continue

        if line.lower() == "config":
            print("Current Rate Limiting Configuration:")
            print(f"  • Maximum Requests : {RATE_LIMIT}")
            print(f"  • Time Window      : {TIME_WINDOW} seconds")
            continue

        if line.lower() == "reset":
            limiter.user_requests.clear()
            print("System Reset: All stored request records have been cleared.")
            continue

        try:

            user = parse_request(line)

            timestamp = int(time.time())

            allowed, count = limiter.allow_request(user, timestamp)

            current_time = datetime.datetime.now().strftime("%H:%M:%S")

            if allowed:
                remaining = RATE_LIMIT - count
                message = f"[{current_time}] Request received from '{user}' → ALLOWED ({count}/{RATE_LIMIT}) | Remaining quota: {remaining}"
            else:
                message = f"[{current_time}] Request received from '{user}' → BLOCKED (rate limit exceeded)"

            print(message)

            log_file.write(f"{current_time} {user} {allowed}\n")
            log_file.flush()

        except ValueError as e:
            print(f"Input Error: {e}")
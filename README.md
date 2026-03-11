# API Rate Limiter Simulator

## Overview

This project simulates a backend API rate limiting system that controls how many requests a user can send within a fixed time window.
Rate limiting is commonly used in real-world systems to prevent abuse, protect servers from excessive traffic, and ensure fair resource usage.

The simulator allows users to generate requests from different users and observes whether the requests are **allowed** or **blocked** based on the configured limits.

---

## Problem Decomposition

The project is organized into small modules, each responsible for a single task.

| File                | Responsibility                                  |
| ------------------- | ----------------------------------------------- |
| `main.py`           | Entry point of the application                  |
| `simulator.py`      | Handles user input and runs the simulation loop |
| `rate_limiter.py`   | Core rate limiting logic                        |
| `request_parser.py` | Validates and parses incoming requests          |
| `config.py`         | Stores configurable system parameters           |

This separation improves maintainability, readability, and scalability.

---

## Design Decisions

### Sliding Window Rate Limiting

The system uses the **Sliding Window Algorithm** to track user requests within a time window.

This approach ensures:

* accurate request tracking
* dynamic removal of expired requests
* efficient request evaluation

### Configurable System Parameters

Rate limiting parameters are separated into a configuration file (`config.py`) so the system behavior can be modified without changing the core logic.

Example:

RATE_LIMIT = 5
TIME_WINDOW = 60 seconds

---

## Data Structures and Algorithms

### Dictionary

Used to map users to their request history.

Example structure:

{
"user1": [timestamps],
"user2": [timestamps]
}

This allows fast lookup for each user's requests.

### Deque (Double Ended Queue)

Each user’s requests are stored using a **deque**.

Reasons:

* efficient removal from the front (O(1))
* ideal for sliding window cleanup
* better performance than a normal list

### Algorithm Complexity

Time Complexity: **O(1)** per request
Space Complexity: **O(n)** where *n* is the number of stored requests.

---

## Features

The simulator provides the following capabilities:

• Simulate user requests
• Real-time timestamps for each request
• Track request count per user
• Display remaining allowed requests
• Show active user statistics
• Reset rate limit data
• Configurable rate limit settings
• Request logging to a file

---

## Example Execution

Start the simulator:

python main.py

Example interaction:

> alice
> [15:45:01] Request from alice → ALLOWED (1/5) | Remaining: 4

> alice
> [15:45:02] Request from alice → ALLOWED (2/5) | Remaining: 3

> stats
> Active users being tracked: 1

> config
> Rate Limit: 5 requests
> Time Window: 60 seconds

> alice
> [15:45:06] Request from alice → BLOCKED (limit reached)

---

## How to Build and Run

1. Clone the repository

git clone https://github.com/GPahuja67/Rate-Limiter.git

2. Navigate to the project directory

cd Rate-Limiter

3. Run the simulator

python main.py

No external dependencies are required.

---

## Edge Cases Handled

The system handles several edge cases including:

• empty or invalid user input
• malformed commands
• request bursts from the same user
• multiple users sending requests simultaneously

Expired requests are automatically removed from the sliding window.

---

## Trade-offs and Limitations

• The system stores request data **in memory**, so it is not persistent across restarts.
• It simulates request traffic rather than integrating with a real API gateway.
• The simulator assumes timestamps from the system clock and does not handle distributed system clock drift.

---

## Possible Future Improvements

• Persistent storage using Redis or a database
• Distributed rate limiting across multiple servers
• REST API interface instead of CLI input
• Visualization dashboard for request traffic

---

## Conclusion

This project demonstrates a modular implementation of a rate limiting system using a sliding window algorithm.
The design focuses on **clean architecture, efficient data structures, and clear separation of responsibilities**, reflecting common patterns used in backend systems.

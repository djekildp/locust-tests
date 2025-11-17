# Performance Testing Task

## Objective

Evaluate your ability to work with performance testing frameworks and Python programming by enhancing an existing test suite.

## Setup

1. Clone this repository
2. Configure your development environment to run the tests
3. Familiarize yourself with the existing test structure in `simulations/demo_locustfile.py`
4. The tests target the JSONPlaceholder API: <https://jsonplaceholder.typicode.com>

## Task Requirements

### Part 1: Dynamic User Assignment

Currently, the test uses a hardcoded `user_id = 1`. Your task is to:

- Read user IDs from the provided data file (`simulations/users.csv` or `simulations/users.json`)
- Assign a unique user ID to each simulated user in a round-robin fashion
- Ensure that when user data runs out, it cycles back to the beginning

### Part 2: Data-Driven Testing

Modify the test flow to make it more realistic:

- Update the `get_posts` task to:
  - Fetch posts for the assigned user
  - Extract and store the post IDs from the response
- Update the `get_comments` task to:
  - Use post IDs obtained from the user's actual posts (from `get_posts` response)
  - Instead of using the hardcoded `self.post_ids` list

## Expected Behavior

- Each simulated user should have their own user ID
- Comments should only be requested for posts that actually belong to that user
- The test should handle API responses appropriately

## Advanced Task (Bonus)

### Part 3: Distributed Data Management

Implement a master-worker data distribution system for running tests in distributed mode:

**Requirements:**

- The master process should:
  - Read the entire data file on startup
  - Listen for data requests from worker processes
  - Distribute user IDs to workers
  - Handle worker reconnections and data reassignment

- Worker processes should:
  - Request user data from the master on startup
  - Use the assigned user IDs for test execution
  - Handle cases where master is unavailable

**Implementation Notes:**

- Use Locust's built-in messaging system between master and workers
- Ensure thread-safe data distribution
- Consider what happens when workers exceed available user IDs
- Document your approach and any assumptions made

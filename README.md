# Task list report creator

The Task list report creator application takes as input a JSON file with task
 information, performs various calculations on it, and prints the results.

## Input data
Input data to the application is in form of a JSON file with the following
 structure:

```json
{
    "tasks": [
        {
            "name": "X", // Name of task
            "duration_ms": 1000, // How long the task took to run, in milliseconds
            "average_cpu_cores": 0.5, // Average number of CPU cores consumed by this task
            "average_memory_mb": 100 // Average RAM usage of this task
        }
        // ...more tasks
    ]
}
```

## How to install and run

1. Recommended: Install and activate a Python virtual environment
2. Install requirements `pip install -r requirements.txt`
3. Run the program with input `python program.py data.json`

How to run tests

Using the same virtual environment as above, run:
`pytest test_program.py`

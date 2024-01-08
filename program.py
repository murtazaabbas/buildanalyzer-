"""task.py list report creator."""

import sys
import os
import json

from task import Task
from analyzer_type import AnalyzerType
from build_analyzer import BuildAnalyzer


def main():
    # Check arguments
    if not sys.argv:
        print("Error: Please provide data file to read.")
        return

    path = sys.argv[1]

    if not os.path.exists(path):
        print("Error: Provided data file does not exist")
        return

    # Load data
    with open(path) as json_file:
        json_data = json.load(json_file)
    tasks = [Task(**x) for x in json_data["tasks"]]

    # Print tasks by duration
    analyzer = BuildAnalyzer(tasks)
    tasks_by_duration = analyzer.analyz_data(AnalyzerType.MAX_CPU)
    for task in tasks_by_duration:
        print(f"task.py: {task.name}, duration: {task.duration_ms}")


if __name__ == "__main__":
    main()

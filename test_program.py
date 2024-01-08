"""Tests for task list report creator."""
import pytest

from task import Task
from analyzer_type import AnalyzerType
from build_analyzer import BuildAnalyzer

tasks = [
    Task(name="Longest", duration_ms=100, average_cpu_cores=4, average_memory_mb=512),
    Task(name="Shortest", duration_ms=1, average_cpu_cores=2, average_memory_mb=1024)
]
analyzer = BuildAnalyzer(tasks)


def test_sort_by_duration():
    sorted_tasks = analyzer.analyz_data(AnalyzerType.MIN_TIME)
    assert sorted_tasks[0].name == "Shortest"


def test_average_cpu():
    average_cpu = analyzer.analyz_data(AnalyzerType.AVERAGE_MEMORY)
    print(average_cpu)
    assert average_cpu > 1


def test_analyz_data_with_invalid():
    with pytest.raises(Exception) as excinfo:
        analyzer.analyz_data(None)
    assert str(excinfo.value) == 'attribute_type is invalid'


def test_remove_duplicate_by_name():
    tasks = [
        Task(name="Longest", duration_ms=100, average_cpu_cores=4, average_memory_mb=512),
        Task(name="Shortest", duration_ms=1, average_cpu_cores=2, average_memory_mb=1024),
        Task(name="Shortest", duration_ms=2, average_cpu_cores=2, average_memory_mb=1024)
    ]
    analyzer = BuildAnalyzer(tasks)
    unique_tasks = analyzer.analyz_data(AnalyzerType.REMOVE_DEPLICATE)
    print(unique_tasks)
    assert len(unique_tasks) > 0


def test_total_task_calculation():
    tasks = [
        Task(name="Longest", duration_ms=100, average_cpu_cores=4, average_memory_mb=512),
        Task(name="Shortest", duration_ms=1, average_cpu_cores=2, average_memory_mb=1024),
        Task(name="Shortest", duration_ms=2, average_cpu_cores=2, average_memory_mb=1024)
    ]
    analyzer = BuildAnalyzer(tasks)
    total_calculated_sum = analyzer.analyz_data(AnalyzerType.TOTAL_CALCULATION)
    print(total_calculated_sum)
    assert len(total_calculated_sum) > 0

def test_total_task_calculation():
    tasks = [
        Task(name="Longest", duration_ms=100, average_cpu_cores=4, average_memory_mb=512),
        Task(name="Shortest", duration_ms=1, average_cpu_cores=2, average_memory_mb=2048),
        Task(name="Shortest", duration_ms=2, average_cpu_cores=2, average_memory_mb=1024),
        Task(name="Shortest", duration_ms=10, average_cpu_cores=2, average_memory_mb=1024),
        Task(name="Shortest", duration_ms=5, average_cpu_cores=2, average_memory_mb=256)
    ]
    analyzer = BuildAnalyzer(tasks)
    total_calculated_sum = analyzer.analyz_data(AnalyzerType.MULTIPLE_FIELDS_SORTING)
    print(total_calculated_sum)
    assert len(total_calculated_sum) > 0

def test_task_filters():
    tasks = [
        Task(name="Longest", duration_ms=100, average_cpu_cores=4, average_memory_mb=512),
        Task(name="Shortest", duration_ms=1, average_cpu_cores=2, average_memory_mb=2048),
        Task(name="Shortest", duration_ms=2, average_cpu_cores=2, average_memory_mb=1024),
        Task(name="Shortest", duration_ms=10, average_cpu_cores=2, average_memory_mb=1024),
        Task(name="Shortest", duration_ms=5, average_cpu_cores=2, average_memory_mb=256)
    ]
    analyzer = BuildAnalyzer(tasks)
    print(analyzer)
    total_calculated_sum = analyzer.analyz_data(AnalyzerType.TASK_FILTERS)
    # print(total_calculated_sum)
    assert len(total_calculated_sum) > 0

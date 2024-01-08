from concurrent.futures.thread import ThreadPoolExecutor
from typing import List

from task import Task
from analyzer_type import AnalyzerType


class BuildAnalyzer:
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks

    def __sort_by_duration(self, sort_order=False) -> List[Task]:
        """Sorts a task list by duration, the lowest duration first."""
        return sorted(self.tasks, key=lambda x: x.duration_ms, reverse=sort_order)

    def __average_memory(self) -> float:
        """Calculates the average memory utilization across all tasks."""
        total_memory = sum(task.average_memory_mb for task in self.tasks)
        return total_memory / len(self.tasks) if len(self.tasks) > 0 else 0

    def __remove_duplicate_by_name(self) -> List[Task]:
        task_set = set()
        unique_tasks = list()
        for task in self.tasks:
            if task.name not in task_set:
                unique_tasks.append(task)
            task_set.add(task.name)
        return unique_tasks

    def __total_caculation(self) -> tuple:
        with ThreadPoolExecutor(max_workers=3) as executor:
            results = list(executor.map(self.calculate_sum, self.tasks))

        # Calculate the total sum for each attribute
        total_duration_ms = sum(result[0] for result in results)
        total_average_cpu_cores = sum(result[1] for result in results)
        total_average_memory_mb = sum(result[2] for result in results)

        return (total_duration_ms, total_average_cpu_cores, total_average_memory_mb)

    def __calculate_sum(self, task: Task):
        return (
            task.duration_ms,
            task.average_cpu_cores,
            task.average_memory_mb,
        )

    def __multiple_field_sort(self) -> List[Task]:
        return sorted(self.tasks, key=lambda x: (x.duration_ms, x.average_memory_mb), reverse=True)

    def __task_filters(self) -> List[Task]:
        filter_conditions = [
            lambda task: task.duration_ms > 5,
            lambda task: task.average_memory_mb > 512
        ]
        filtered_tasks = self.tasks
        for condition in filter_conditions:
            filtered_tasks = filter(condition, filtered_tasks)
        return list(filtered_tasks)

    def __repr__(self):
        return str(self.tasks)

    def analyz_data(self, attribute_type: AnalyzerType, sort_order=False):
        if attribute_type is None or attribute_type not in AnalyzerType:
            raise Exception("attribute_type is invalid")

        if attribute_type.value == AnalyzerType.MIN_TIME.value:
            return self.__sort_by_duration(sort_order=sort_order)

        if attribute_type.value == AnalyzerType.AVERAGE_MEMORY.value:
            return self.__average_memory()

        if attribute_type.value == AnalyzerType.REMOVE_DEPLICATE.value:
            return self.__remove_duplicate_by_name()

        if attribute_type.value == AnalyzerType.TOTAL_CALCULATION.value:
            return self.__total_caculation()

        if attribute_type.value == AnalyzerType.MULTIPLE_FIELDS_SORTING.value:
            return self.__multiple_field_sort()

        if attribute_type.value == AnalyzerType.TASK_FILTERS.value:
            return self.__task_filters()

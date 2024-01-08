from enum import Enum


class AnalyzerType(Enum):
    MIN_CPU = 1
    AVERAGE_MEMORY = 2
    MAX_CPU = 3
    MIN_TIME = 4
    REMOVE_DEPLICATE = 5
    TOTAL_CALCULATION = 6
    MULTIPLE_FIELDS_SORTING = 7
    TASK_FILTERS = 8

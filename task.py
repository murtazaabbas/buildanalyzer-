from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    name: str
    duration_ms: int
    average_cpu_cores: float
    average_memory_mb: int

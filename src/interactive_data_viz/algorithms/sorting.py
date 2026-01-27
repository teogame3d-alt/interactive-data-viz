from __future__ import annotations

from typing import Generator, List

from .metrics import Metrics


def bubble_sort(data: List[int], metrics: Metrics) -> Generator[List[int], None, None]:
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            metrics.compare()
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                metrics.swap()
                yield arr[:]
    yield arr

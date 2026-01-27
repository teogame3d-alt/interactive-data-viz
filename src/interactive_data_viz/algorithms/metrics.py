from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Metrics:
    comparisons: int = 0
    swaps: int = 0

    def compare(self) -> None:
        self.comparisons += 1

    def swap(self) -> None:
        self.swaps += 1

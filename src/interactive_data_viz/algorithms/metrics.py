from __future__ import annotations

"""RO: Metrice simple pentru comparatii si swap-uri.
EN: Simple metrics for comparisons and swaps.
"""

from dataclasses import dataclass


@dataclass
class Metrics:
    """RO: Colecteaza statistici in timpul sortarii.
    EN: Collects stats during sorting.
    """
    comparisons: int = 0
    swaps: int = 0

    def compare(self) -> None:
        """RO: Incrementeaza numarul de comparatii.
        EN: Increment comparison count.
        """
        self.comparisons += 1

    def swap(self) -> None:
        """RO: Incrementeaza numarul de swap-uri.
        EN: Increment swap count.
        """
        self.swaps += 1

from __future__ import annotations

"""RO: Incarcarea dataset-ului din CSV.
EN: Load dataset from CSV.
"""

from pathlib import Path
import pandas as pd


def load_data(path: Path) -> pd.DataFrame:
    """RO: Citeste CSV in DataFrame.
    EN: Read CSV into a DataFrame.
    """
    return pd.read_csv(path)

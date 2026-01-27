from __future__ import annotations

from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class DataContract:
    required_columns: tuple[str, ...]
    numeric_columns: tuple[str, ...]
    categorical_columns: tuple[str, ...]
    ranges: dict[str, tuple[float, float]]


def validate_schema(df: pd.DataFrame, contract: DataContract) -> list[str]:
    errors: list[str] = []
    for col in contract.required_columns:
        if col not in df.columns:
            errors.append(f"Missing column: {col}")
    for col in contract.numeric_columns:
        if col in df.columns and not pd.api.types.is_numeric_dtype(df[col]):
            errors.append(f"Column not numeric: {col}")
    for col, (min_v, max_v) in contract.ranges.items():
        if col in df.columns:
            bad = df[col].dropna().between(min_v, max_v)
            if not bad.all():
                errors.append(f"Out of range values in {col}")
    return errors

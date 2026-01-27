from pathlib import Path
import pandas as pd

from interactive_data_viz.cleaning_pipeline.cleaner import clean_missing
from interactive_data_viz.cleaning_pipeline.validator import DataContract, validate_schema


def test_clean_missing() -> None:
    df = pd.DataFrame({"age": [10, None], "name": ["A", None]})
    df2 = clean_missing(df)
    assert df2["age"].isna().sum() == 0
    assert df2["name"].isna().sum() == 0


def test_validate_schema() -> None:
    df = pd.DataFrame({"age": [10], "grade": [5]})
    contract = DataContract(
        required_columns=("age", "grade"),
        numeric_columns=("age", "grade"),
        categorical_columns=(),
        ranges={"age": (0, 120), "grade": (1, 10)},
    )
    assert validate_schema(df, contract) == []

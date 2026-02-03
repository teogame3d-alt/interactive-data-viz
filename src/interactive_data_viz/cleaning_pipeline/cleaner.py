from __future__ import annotations

"""RO: Curata valorile lipsa cu strategii simple.
EN: Clean missing values with simple strategies.
"""

import pandas as pd


def clean_missing(df: pd.DataFrame) -> pd.DataFrame:
    """RO: Completeaza numeric cu mediana si categoric cu 'Unknown'.
    EN: Fill numeric with median and categorical with 'Unknown'.
    """
    df_fill = df.copy()

    for col in df_fill.select_dtypes(include=["number"]).columns:
        median = df_fill[col].median()
        df_fill[col] = df_fill[col].fillna(median)

    for col in df_fill.select_dtypes(include=["object"]).columns:
        df_fill[col] = df_fill[col].fillna("Unknown")

    df_fill_years = df_fill.copy()
    return df_fill_years

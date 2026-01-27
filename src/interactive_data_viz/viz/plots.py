from __future__ import annotations

import matplotlib.pyplot as plt
import mplcursors
import pandas as pd


def scatter_with_cursor(df: pd.DataFrame, x: str, y: str) -> None:
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title("Interactive scatter")
    cursor = mplcursors.cursor(ax, hover=True)
    @cursor.connect("add")
    def on_add(sel):  # type: ignore
        sel.annotation.set_text(f"{x}={sel.target[0]:.2f}\n{y}={sel.target[1]:.2f}")
    plt.show()

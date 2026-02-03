from __future__ import annotations

"""RO: Ploturi interactive cu mplcursors pentru inspectare rapida.
EN: Interactive plots with mplcursors for quick inspection.
"""

import matplotlib.pyplot as plt
import mplcursors
import pandas as pd


def scatter_with_cursor(df: pd.DataFrame, x: str, y: str) -> None:
    """RO: Scatter interactiv cu tooltip-uri la hover.
    EN: Interactive scatter with hover tooltips.
    """
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title("Interactive scatter")
    cursor = mplcursors.cursor(ax, hover=True)
    @cursor.connect("add")
    def on_add(sel):  # type: ignore
        # RO: Afiseaza valorile exacte ale punctului selectat.
        # EN: Show exact values for the selected point.
        sel.annotation.set_text(f"{x}={sel.target[0]:.2f}\n{y}={sel.target[1]:.2f}")
    plt.show()

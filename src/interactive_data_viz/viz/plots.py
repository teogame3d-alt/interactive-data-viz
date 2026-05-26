from __future__ import annotations

"""RO: Ploturi interactive cu mplcursors pentru inspectare rapida.
EN: Interactive plots with mplcursors for quick inspection.
"""

import matplotlib.pyplot as plt
import mplcursors
import pandas as pd
from pathlib import Path


def scatter_with_cursor(df: pd.DataFrame, x: str, y: str) -> None:
    """RO: Scatter interactiv cu tooltip-uri la hover.
    EN: Interactive scatter with hover tooltips.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor("#eef3f6")
    ax.set_facecolor("#ffffff")
    ax.scatter(df[x], df[y], s=90, color="#0f766e", edgecolor="#172033", linewidth=0.8)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title("Interactive student quality scatter", fontweight="bold")
    ax.grid(True, color="#d8e2ea", linewidth=0.8)
    cursor = mplcursors.cursor(ax, hover=True)

    @cursor.connect("add")
    def on_add(sel):  # type: ignore
        # RO: Afiseaza valorile exacte ale punctului selectat.
        # EN: Show exact values for the selected point.
        sel.annotation.set_text(f"{x}={sel.target[0]:.2f}\n{y}={sel.target[1]:.2f}")

    plt.show()


def save_quality_dashboard(df: pd.DataFrame, out_path: Path) -> Path:
    """Save a polished static dashboard used by the public README screenshots.

    The interactive chart is excellent for live exploration, but a recruiter
    reviewing GitHub first needs a deterministic image. This helper renders the
    same data story as a stable PNG: grade distribution, average by group, and
    a compact data-quality summary.
    """

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(12.8, 7.2), facecolor="#eef3f6")
    grid = fig.add_gridspec(2, 3, height_ratios=[0.85, 1.25], hspace=0.35, wspace=0.28)

    title_ax = fig.add_subplot(grid[0, :2])
    title_ax.axis("off")
    title_ax.text(
        0.0,
        0.72,
        "Interactive Data Viz",
        fontsize=26,
        fontweight="bold",
        color="#172033",
    )
    title_ax.text(
        0.0,
        0.42,
        "ETL pipeline, schema validation, missing-value handling, and visual analytics.",
        fontsize=13,
        color="#4b5b6d",
    )
    title_ax.text(
        0.0,
        0.12,
        "Portfolio signal: data is checked before it is charted.",
        fontsize=12,
        color="#0f766e",
        fontweight="bold",
    )

    metric_ax = fig.add_subplot(grid[0, 2])
    metric_ax.set_facecolor("#172033")
    metric_ax.set_xticks([])
    metric_ax.set_yticks([])
    for spine in metric_ax.spines.values():
        spine.set_visible(False)
    missing_total = int(df.isna().sum().sum())
    metric_lines = [
        ("Rows", len(df)),
        ("Columns", len(df.columns)),
        ("Missing values", missing_total),
        ("Avg grade", f"{df['grade'].mean():.2f}"),
    ]
    for idx, (label, value) in enumerate(metric_lines):
        y = 0.78 - idx * 0.22
        metric_ax.text(
            0.08, y, label.upper(), color="#9fb5c8", fontsize=9, fontweight="bold"
        )
        metric_ax.text(
            0.62, y, str(value), color="#ffffff", fontsize=18, fontweight="bold"
        )

    hist_ax = fig.add_subplot(grid[1, 0])
    hist_ax.hist(df["grade"], bins=5, color="#0f766e", edgecolor="#172033", alpha=0.9)
    hist_ax.set_title("Grade Distribution", fontweight="bold", color="#172033")
    hist_ax.set_xlabel("grade")
    hist_ax.set_ylabel("count")
    hist_ax.grid(True, axis="y", color="#d8e2ea")

    group_ax = fig.add_subplot(grid[1, 1])
    group_mean = df.groupby("group")["grade"].mean().sort_index()
    group_ax.bar(
        group_mean.index, group_mean.values, color=["#0f766e", "#2563eb", "#b7791f"]
    )
    group_ax.set_title("Average Grade by Group", fontweight="bold", color="#172033")
    group_ax.set_ylim(0, 10)
    group_ax.grid(True, axis="y", color="#d8e2ea")

    scatter_ax = fig.add_subplot(grid[1, 2])
    scatter_ax.scatter(
        df["age"], df["grade"], s=100, color="#2563eb", edgecolor="#172033"
    )
    scatter_ax.set_title("Age vs Grade", fontweight="bold", color="#172033")
    scatter_ax.set_xlabel("age")
    scatter_ax.set_ylabel("grade")
    scatter_ax.grid(True, color="#d8e2ea")

    fig.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return out_path

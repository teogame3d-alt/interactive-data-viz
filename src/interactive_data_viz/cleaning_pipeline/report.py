from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def generate_report(df: pd.DataFrame, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / "report.md"

    summary = df.describe(include="all").transpose()
    missing = df.isna().sum()

    fig, ax = plt.subplots(figsize=(6, 4))
    missing.plot(kind="bar", ax=ax)
    ax.set_title("Missing values per column")
    fig.tight_layout()
    img_path = out_dir / "missing.png"
    fig.savefig(img_path)
    plt.close(fig)

    report_path.write_text(
        "# Data Report\n\n"
        "## Summary\n\n"
        f"{summary.to_markdown()}\n\n"
        "## Missing Values\n\n"
        f"{missing.to_markdown()}\n\n"
        f"![missing]({img_path.name})\n",
        encoding="utf-8",
    )
    return report_path

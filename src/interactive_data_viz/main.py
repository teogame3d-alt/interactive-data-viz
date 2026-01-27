from __future__ import annotations

from pathlib import Path
import random

from .cleaning_pipeline.loader import load_data
from .cleaning_pipeline.validator import DataContract, validate_schema
from .cleaning_pipeline.cleaner import clean_missing
from .cleaning_pipeline.report import generate_report
from .viz.plots import scatter_with_cursor
from .viz.sorting_animator import SortingAnimator
from .algorithms.bst import insert, inorder, height, count_nodes, sum_tree
from .viz.tree_visualizer import draw_tree


def main() -> None:
    base = Path(__file__).resolve().parents[2]
    data_path = base / "data" / "demo_students.csv"

    df = load_data(data_path)
    contract = DataContract(
        required_columns=("name", "age", "grade", "year", "group"),
        numeric_columns=("age", "grade", "year"),
        categorical_columns=("name", "group"),
        ranges={"age": (10, 100), "grade": (1, 10), "year": (2000, 2030)},
    )
    errors = validate_schema(df, contract)
    if errors:
        print("Schema errors:")
        for e in errors:
            print("-", e)
    df_clean = clean_missing(df)
    report_path = generate_report(df_clean, base / "reports")
    print(f"Report generated: {report_path}")

    scatter_with_cursor(df_clean, "age", "grade")

    SortingAnimator(size=25).show()

    root = None
    for v in random.sample(range(1, 40), 10):
        root = insert(root, v)
    print("BST inorder:", inorder(root))
    print("Height:", height(root), "Nodes:", count_nodes(root), "Sum:", sum_tree(root))
    draw_tree(root)


if __name__ == "__main__":
    main()

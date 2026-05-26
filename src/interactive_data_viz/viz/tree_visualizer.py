from __future__ import annotations

"""RO: Vizualizare simpla pentru un arbore BST.
EN: Simple visualization for a BST.
"""

import matplotlib.pyplot as plt

from ..algorithms.bst import Node


def _layout(node: Node | None, x: float, y: float, dx: float, positions: dict[Node, tuple[float, float]]):
    """RO: Calculeaza recursiv coordonatele fiecarui nod.
    EN: Recursively compute node positions.
    """
    if node is None:
        return
    positions[node] = (x, y)
    _layout(node.left, x - dx, y - 1, dx / 2, positions)
    _layout(node.right, x + dx, y - 1, dx / 2, positions)


def draw_tree(root: Node | None) -> None:
    """RO: Deseneaza arborele folosind Matplotlib.
    EN: Draw the tree using Matplotlib.
    """
    if root is None:
        return
    positions: dict[Node, tuple[float, float]] = {}
    _layout(root, 0.0, 0.0, 1.0, positions)

    fig, ax = plt.subplots()
    for node, (x, y) in positions.items():
        ax.text(x, y, str(node.value), ha="center", va="center",
                bbox=dict(boxstyle="round", facecolor="lightblue"))
        if node.left:
            lx, ly = positions[node.left]
            ax.plot([x, lx], [y, ly], color="gray")
        if node.right:
            rx, ry = positions[node.right]
            ax.plot([x, rx], [y, ry], color="gray")

    ax.axis("off")
    plt.show()

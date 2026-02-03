from __future__ import annotations

"""RO: Operatii de baza pentru un BST (insert/inorder/etc).
EN: Basic BST operations (insert/inorder/etc).
"""

from dataclasses import dataclass


@dataclass
class Node:
    """RO: Nod BST simplu.
    EN: Simple BST node.
    """
    value: int
    left: "Node | None" = None
    right: "Node | None" = None


def insert(root: Node | None, value: int) -> Node:
    """RO: Insereaza o valoare in BST.
    EN: Insert a value into the BST.
    """
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def inorder(root: Node | None) -> list[int]:
    """RO: Traversare inorder (sortata).
    EN: Inorder traversal (sorted order).
    """
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def height(root: Node | None) -> int:
    """RO: Inaltimea arborelui.
    EN: Tree height.
    """
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def count_nodes(root: Node | None) -> int:
    """RO: Numar total de noduri.
    EN: Total node count.
    """
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def sum_tree(root: Node | None) -> int:
    """RO: Suma valorilor din arbore.
    EN: Sum of values in the tree.
    """
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

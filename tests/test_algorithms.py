from interactive_data_viz.algorithms.metrics import Metrics
from interactive_data_viz.algorithms.sorting import bubble_sort
from interactive_data_viz.algorithms.bst import insert, inorder


def test_bubble_sort() -> None:
    metrics = Metrics()
    data = [3, 2, 1]
    frames = list(bubble_sort(data, metrics))
    assert frames[-1] == [1, 2, 3]
    assert metrics.comparisons > 0


def test_bst_inorder() -> None:
    root = None
    for v in [3, 1, 4, 2]:
        root = insert(root, v)
    assert inorder(root) == [1, 2, 3, 4]

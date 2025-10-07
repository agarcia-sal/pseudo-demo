from typing import Any, List, Sequence


def filter_integers(collection: Sequence[Any]) -> List[int]:
    def helper(index: int, acc: List[int]) -> List[int]:
        if index >= len(collection):
            return acc
        current_element = collection[index]
        new_acc = acc + [current_element] if isinstance(current_element, int) else acc
        return helper(index + 1, new_acc)

    return helper(0, [])
from typing import List, Any


def filter_integers(list_of_values: List[Any]) -> List[int]:
    def helper(index: int, collected: List[int]) -> List[int]:
        if index >= len(list_of_values):
            return collected
        current = list_of_values[index]
        if not isinstance(current, int):
            return helper(index + 1, collected)
        appended = collected + [current]
        return helper(index + 1, appended)

    return helper(0, [])
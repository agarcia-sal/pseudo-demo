from typing import Any, List, Sequence


def filter_integers(valuesCollection: Sequence[Any]) -> List[int]:
    def helper(index: int) -> List[int]:
        if index >= len(valuesCollection):
            return []
        currentItem = valuesCollection[index]
        restFiltered = helper(index + 1)
        if isinstance(currentItem, int):
            return [currentItem] + restFiltered
        else:
            return restFiltered

    return helper(0)
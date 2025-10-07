from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    result_collection: List[int] = []

    def helper(idx: int) -> None:
        if idx >= len(list_of_values):
            return
        candidate = list_of_values[idx]
        if not isinstance(candidate, int):
            helper(idx + 1)
            return
        result_collection.append(candidate)
        helper(idx + 1)

    helper(0)
    return result_collection
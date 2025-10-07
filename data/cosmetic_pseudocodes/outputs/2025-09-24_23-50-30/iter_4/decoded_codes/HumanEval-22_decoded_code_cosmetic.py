from typing import List, Any


def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_list: List[int] = []

    def iterate(index: int) -> None:
        if index >= len(list_of_values):
            return
        if isinstance(list_of_values[index], int):
            filtered_list.append(list_of_values[index])
        iterate(index + 1)

    iterate(0)
    return filtered_list
from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    def is_integer_type(value: Any) -> bool:
        return type(value) is int

    def collect_integers(index: int, accumulator: List[int]) -> List[int]:
        if index >= len(list_of_values):
            return accumulator
        if is_integer_type(list_of_values[index]):
            return collect_integers(index + 1, accumulator + [list_of_values[index]])
        return collect_integers(index + 1, accumulator)

    return collect_integers(0, [])
from typing import Iterable, List, TypeVar
from collections import Counter

T = TypeVar('T')

def remove_duplicates(arb_input: Iterable[T]) -> List[T]:
    freq_map: Counter = Counter(arb_input)
    filtered_result: List[T] = []
    idx: int = 0
    input_list = list(arb_input)  # ensure indexing capability
    while idx < len(input_list):
        current_item = input_list[idx]
        if freq_map[current_item] <= 1:
            filtered_result.append(current_item)
        idx += 1
    return filtered_result
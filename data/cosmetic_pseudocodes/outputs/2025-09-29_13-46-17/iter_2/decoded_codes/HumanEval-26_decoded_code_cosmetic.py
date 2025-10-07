from typing import List
from collections import Counter

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    freq_map: Counter[int] = Counter(list_of_numbers)
    result_list: List[int] = []

    def helper(index: int) -> None:
        if index >= len(list_of_numbers):
            return
        current = list_of_numbers[index]
        if freq_map[current] <= 1:
            result_list.append(current)
        helper(index + 1)

    helper(0)
    return result_list
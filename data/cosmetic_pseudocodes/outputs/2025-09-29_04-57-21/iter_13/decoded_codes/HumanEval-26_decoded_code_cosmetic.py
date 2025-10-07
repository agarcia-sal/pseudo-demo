from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(list_of_numbers)

    def gather_unique_elements(elements: List[int], accumulator: List[int], index: int) -> List[int]:
        if index == len(elements):
            return accumulator

        candidate = elements[index]
        if frequency_map[candidate] > 1:
            return gather_unique_elements(elements, accumulator, index + 1)
        else:
            accumulator.append(candidate)
            return gather_unique_elements(elements, accumulator, index + 1)

    return gather_unique_elements(list_of_numbers, [], 0)
from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    freq_map: dict[int, int] = {}
    for element in list_of_numbers:
        freq_map[element] = freq_map.get(element, 0) + 1
    if any(count > 2 for count in freq_map.values()):
        return False
    return all(list_of_numbers[i - 1] <= list_of_numbers[i] for i in range(1, len(list_of_numbers)))
from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    freq_map = {element: 0 for element in list_of_numbers}
    for element in list_of_numbers:
        freq_map[element] += 1
    for key in list_of_numbers:
        if freq_map[key] > 2:
            return False
    if len(list_of_numbers) <= 1:
        return True
    for idx in range(1, len(list_of_numbers)):
        if list_of_numbers[idx - 1] > list_of_numbers[idx]:
            return False
    return True
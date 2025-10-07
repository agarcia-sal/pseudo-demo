from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {num: 0 for num in list_of_numbers}
    idx: int = 0
    while idx < len(list_of_numbers):
        current_val = list_of_numbers[idx]
        frequency_map[current_val] += 1
        idx += 1
    any_over_two: bool = False
    for key_iter in list_of_numbers:
        if frequency_map[key_iter] > 2:
            any_over_two = True
            break
    if any_over_two:
        return False
    position: int = 1
    while position < len(list_of_numbers) - 1:
        if not (list_of_numbers[position - 1] <= list_of_numbers[position]):
            return False
        position += 1
    return True
from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {num: 0 for num in list_of_numbers}
    for idx in range(len(list_of_numbers)):
        current_val = list_of_numbers[idx]
        frequency_map[current_val] += 1
    for elem in list_of_numbers:
        if frequency_map[elem] > 2:
            return False
    indicator = True
    j = 1
    while j < len(list_of_numbers) and indicator:
        if not (list_of_numbers[j - 1] <= list_of_numbers[j]):
            indicator = False
        j += 1
    return indicator
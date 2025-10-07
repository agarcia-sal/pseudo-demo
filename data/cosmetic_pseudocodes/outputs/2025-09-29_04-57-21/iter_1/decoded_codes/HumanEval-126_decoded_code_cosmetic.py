from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {num: 0 for num in list_of_numbers}
    for num in list_of_numbers:
        frequency_map[num] += 1

    for key in list_of_numbers:
        if frequency_map[key] > 2:
            return False

    for index in range(1, len(list_of_numbers)):
        if list_of_numbers[index - 1] > list_of_numbers[index]:
            return False

    return True
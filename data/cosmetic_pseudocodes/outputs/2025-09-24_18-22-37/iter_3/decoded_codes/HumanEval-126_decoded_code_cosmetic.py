from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequencies: dict[int, int] = {}
    index = 0
    while index < len(list_of_numbers):
        element = list_of_numbers[index]
        if element not in frequencies:
            frequencies[element] = 1
        else:
            frequencies[element] += 1
        index += 1

    index = 0
    repeat_check = True
    while index < len(list_of_numbers) and repeat_check:
        if frequencies[list_of_numbers[index]] > 2:
            repeat_check = False
        index += 1

    if not repeat_check:
        return False

    index = 1
    while index < len(list_of_numbers):
        if list_of_numbers[index - 1] > list_of_numbers[index]:
            return False
        index += 1

    return True
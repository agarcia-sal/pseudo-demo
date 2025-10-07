from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    registry: dict[int, int] = {element: 0 for element in list_of_numbers}
    for index in range(len(list_of_numbers)):
        element = list_of_numbers[index]
        registry[element] += 1
    for element in list_of_numbers:
        if registry[element] > 2:
            return False
    position = 1
    while position < len(list_of_numbers):
        if not (list_of_numbers[position - 1] <= list_of_numbers[position]):
            return False
        position += 1
    return True
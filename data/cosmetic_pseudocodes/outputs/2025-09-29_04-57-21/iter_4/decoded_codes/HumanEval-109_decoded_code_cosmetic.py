from typing import List


def move_one_ball(input_numbers: List[int]) -> bool:
    if not input_numbers:
        return True

    arranged_numbers: List[int] = sorted(input_numbers)
    smallest_element: int = input_numbers[0]
    position_of_smallest: int = 0

    counter: int = 1
    while counter < len(input_numbers):
        if input_numbers[counter] < smallest_element:
            smallest_element = input_numbers[counter]
            position_of_smallest = counter
        counter += 1

    rotated_version: List[int] = []
    i: int = 0
    length: int = len(input_numbers)
    while i < length:
        idx = (position_of_smallest + i) % length
        rotated_version.append(input_numbers[idx])
        i += 1

    j: int = 0
    while j < length:
        if rotated_version[j] != arranged_numbers[j]:
            return False
        j += 1

    return True
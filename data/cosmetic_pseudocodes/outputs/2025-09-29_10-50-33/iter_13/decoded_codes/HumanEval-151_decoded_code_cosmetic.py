from typing import List


def double_the_difference(list_of_numbers: List[int]) -> int:
    repeat_index: int = 0
    accumulator: int = 0

    while True:
        if repeat_index >= len(list_of_numbers):
            return accumulator

        element: int = list_of_numbers[repeat_index]
        condition_one: bool = element > 0  # not (element <= 0)
        condition_two: bool = element % 2 != 0  # not (element mod 2 = 0)
        condition_three: bool = '.' not in str(element)  # not ("." in to_string(element))
        compound_condition: bool = condition_one and condition_two and condition_three

        if not compound_condition:
            repeat_index += 1
            continue

        accumulator += element * element
        repeat_index += 1
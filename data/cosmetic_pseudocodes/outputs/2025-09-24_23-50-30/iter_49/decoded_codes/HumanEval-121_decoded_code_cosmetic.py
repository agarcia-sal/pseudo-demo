from typing import List

def solution(array_of_numbers: List[int]) -> int:
    def inner_accumulate(position: int, accumulation_value: int) -> int:
        if not (position < len(array_of_numbers)):
            return accumulation_value
        current_element = array_of_numbers[position]
        if (position % 2 == 0) and (current_element % 2 == 1):
            updated_accumulation = accumulation_value + current_element
        else:
            updated_accumulation = accumulation_value
        return inner_accumulate(position + 1, updated_accumulation)

    return inner_accumulate(0, 0)
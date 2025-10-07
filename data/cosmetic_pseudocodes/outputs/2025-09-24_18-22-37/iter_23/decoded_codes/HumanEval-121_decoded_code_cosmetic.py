from typing import List

def solution(array_of_numbers: List[int]) -> int:
    result: int = 0
    pointer: int = 0
    while pointer < len(array_of_numbers):
        current_value = array_of_numbers[pointer]
        if pointer % 2 != 0:
            pointer += 1
            continue
        else:
            if current_value % 2 == 1:
                result += current_value
        pointer += 1
    return result
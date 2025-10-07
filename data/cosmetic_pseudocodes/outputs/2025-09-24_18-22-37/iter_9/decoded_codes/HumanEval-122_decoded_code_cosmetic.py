from typing import List

def add_elements(list_numbers: List[int], number_limit: int) -> int:
    accumulator_result: int = 0
    count_index: int = 0
    while count_index < number_limit:
        current_value: int = list_numbers[count_index]
        string_version: str = str(current_value)
        if not (len(string_version) > 2):
            accumulator_result += current_value
        count_index += 1
    return accumulator_result
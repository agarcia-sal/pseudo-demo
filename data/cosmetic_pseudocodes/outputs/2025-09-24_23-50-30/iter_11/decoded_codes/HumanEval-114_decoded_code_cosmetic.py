from typing import List

def minSubArraySum(array_of_values: List[int]) -> int:
    max_value: int = 0
    temp_accumulator: int = 0
    index: int = 0
    length: int = len(array_of_values)
    while index < length:
        current_element: int = array_of_values[index]
        temp_accumulator += -current_element
        temp_accumulator = max(temp_accumulator, 0)
        max_value = max(max_value, temp_accumulator)
        index += 1
    if max_value == 0:
        reversed_list = [-x for x in array_of_values]
        max_value = max(reversed_list, default=0)
    result: int = -max_value
    return result
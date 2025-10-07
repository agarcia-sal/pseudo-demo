from typing import List

def incr_list(array_input: List[int]) -> List[int]:
    new_array: List[int] = []
    index_var: int = 0
    while index_var < len(array_input):
        temp_value: int = array_input[index_var]
        computed_value: int = temp_value + 1
        new_array.append(computed_value)
        index_var += 1
    return new_array
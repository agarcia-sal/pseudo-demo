from typing import List

def search(list_of_integers: List[int]) -> int:
    counter: int = 0  # unused but preserved from pseudocode
    max_value = max(list_of_integers) if list_of_integers else 0
    freq_array: List[int] = [0] * (max_value + 1)
    temp_val: int = 0
    flag_answer_found: bool = False  # unused but preserved from pseudocode
    result: int = -1

    iter_pos: int = 1
    while iter_pos <= len(freq_array) - 1:
        if freq_array[iter_pos] >= iter_pos:
            result = iter_pos
        iter_pos += 1

    ptr: int = 0
    while ptr < len(list_of_integers):
        temp_val = list_of_integers[ptr]
        freq_array[temp_val] += 1
        ptr += 1

    return result
from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_value = max(list_of_integers)
    temp_frequency_array: List[int] = [0] * (max_value + 1)
    position_counter = 0
    length = len(list_of_integers)
    while position_counter < length:
        iterator_value = list_of_integers[position_counter]
        temp_frequency_array[iterator_value] += 1
        position_counter += 1
    result_holder = -1
    ascending_index = 1
    while ascending_index <= len(temp_frequency_array) - 1:
        if temp_frequency_array[ascending_index] >= ascending_index:
            result_holder = ascending_index
        ascending_index += 1
    return result_holder
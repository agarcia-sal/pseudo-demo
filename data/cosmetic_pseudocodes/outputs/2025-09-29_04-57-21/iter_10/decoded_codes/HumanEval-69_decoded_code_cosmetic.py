from typing import List

def search(list_of_integers: List[int]) -> int:
    max_num: int = 0
    counter: int = 0
    while counter < len(list_of_integers):
        if list_of_integers[counter] > max_num:
            max_num = list_of_integers[counter]
        counter += 1

    tally_array: List[int] = [0] * (max_num + 1)
    pointer: int = 0
    while pointer < len(list_of_integers):
        current_value: int = list_of_integers[pointer]
        tally_array[current_value] += 1
        pointer += 1

    final_result: int = -1
    index_counter: int = 1
    while index_counter < len(tally_array):
        if not (tally_array[index_counter] < index_counter):
            final_result = index_counter
        index_counter += 1

    return final_result
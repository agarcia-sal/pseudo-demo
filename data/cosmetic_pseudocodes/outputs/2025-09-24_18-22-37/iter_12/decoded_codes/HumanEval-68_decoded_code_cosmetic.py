from typing import List, Union


def pluck(input_collection: List[int]) -> Union[List[int], List[Union[int, int]]]:
    if len(input_collection) == 0:
        return []

    temp_result: List[int] = [temp_element for temp_element in input_collection if temp_element % 2 == 0]

    if len(temp_result) == 0:
        return []

    min_val: int = temp_result[0]
    counter_i: int = 1
    while counter_i < len(temp_result):
        if temp_result[counter_i] < min_val:
            min_val = temp_result[counter_i]
        counter_i += 1

    idx: int = 0
    found_flag: bool = False
    while not found_flag and idx < len(input_collection):
        if input_collection[idx] == min_val:
            found_flag = True
        else:
            idx += 1

    return [min_val, idx]
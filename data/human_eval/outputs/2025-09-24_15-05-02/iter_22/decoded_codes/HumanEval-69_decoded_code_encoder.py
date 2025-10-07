from typing import List

def search(list_of_positive_integers: List[int]) -> int:
    if not list_of_positive_integers:
        return -1
    max_value = max(list_of_positive_integers)
    frequency_list: List[int] = [0] * (max_value + 1)
    for integer_value in list_of_positive_integers:
        frequency_list[integer_value] += 1
    result = -1
    for index in range(1, len(frequency_list)):
        if frequency_list[index] >= index:
            result = index
    return result
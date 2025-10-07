from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    length_sum_one = sum(len(string_element) for string_element in list_one)
    length_sum_two = sum(len(string_element) for string_element in list_two)
    if length_sum_one <= length_sum_two:
        return list_one
    else:
        return list_two
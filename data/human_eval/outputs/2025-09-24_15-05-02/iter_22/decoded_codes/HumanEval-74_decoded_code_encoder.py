from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    total_length_one: int = sum(len(string_element) for string_element in list_one)
    total_length_two: int = sum(len(string_element) for string_element in list_two)
    if total_length_one <= total_length_two:
        return list_one
    else:
        return list_two
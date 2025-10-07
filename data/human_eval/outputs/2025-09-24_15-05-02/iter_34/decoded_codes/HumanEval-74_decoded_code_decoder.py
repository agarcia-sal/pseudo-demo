from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    length_one: int = sum(len(string_element) for string_element in list_one)
    length_two: int = sum(len(string_element) for string_element in list_two)
    return list_one if length_one <= length_two else list_two
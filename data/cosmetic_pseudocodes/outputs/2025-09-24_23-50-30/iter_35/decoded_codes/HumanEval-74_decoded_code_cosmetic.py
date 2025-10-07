from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    index_one: int = 0
    length_one: int = 0
    while index_one < len(list_one):
        string_element: str = list_one[index_one]
        length_one += len(string_element)
        index_one += 1

    index_two: int = 0
    length_two: int = 0
    while index_two < len(list_two):
        string_element = list_two[index_two]
        length_two += len(string_element)
        index_two += 1

    if length_one <= length_two:
        return list_one
    else:
        return list_two
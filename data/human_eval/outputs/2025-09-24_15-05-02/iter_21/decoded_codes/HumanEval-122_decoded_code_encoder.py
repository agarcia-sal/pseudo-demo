from typing import List

def add_elements(array_of_integers: List[int], k: int) -> int:
    sum_of_elements = 0
    for index in range(min(k, len(array_of_integers))):
        element = array_of_integers[index]
        string_representation = str(element)
        if len(string_representation) <= 2:
            sum_of_elements += element
    return sum_of_elements
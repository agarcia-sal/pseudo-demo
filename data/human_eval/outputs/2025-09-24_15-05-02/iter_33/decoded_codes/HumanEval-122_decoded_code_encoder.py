from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    sum_of_qualified_elements = 0
    for element in array_of_integers[:integer_k]:
        if len(str(element)) <= 2:
            sum_of_qualified_elements += element
    return sum_of_qualified_elements
from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    sum_result = 0
    limit = min(integer_k, len(array_of_integers))
    for index in range(limit):
        element = array_of_integers[index]
        if len(str(element)) <= 2:
            sum_result += element
    return sum_result
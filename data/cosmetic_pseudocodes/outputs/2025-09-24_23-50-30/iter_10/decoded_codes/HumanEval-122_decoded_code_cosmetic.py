from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    limit: int = integer_k
    subset: List[int] = []
    for index in range(limit):
        subset.append(array_of_integers[index])
    for value in subset:
        if 2 >= len(str(value)):
            accumulator += value
    return accumulator
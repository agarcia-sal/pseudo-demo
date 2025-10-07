from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total = 0
    index = 0
    while index < integer_k:
        current = array_of_integers[index]
        if len(str(current)) <= 2:
            total += current
        index += 1
    return total
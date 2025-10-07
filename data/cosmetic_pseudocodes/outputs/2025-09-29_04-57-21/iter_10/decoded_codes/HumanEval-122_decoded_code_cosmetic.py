from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total: int = 0
    counter: int = 0
    while counter < integer_k:
        current_value: int = array_of_integers[counter]
        if not (len(str(current_value)) > 2):
            total += current_value
        counter += 1
    return total
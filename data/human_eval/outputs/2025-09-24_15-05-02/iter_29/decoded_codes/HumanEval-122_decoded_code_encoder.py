from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    return sum(element for element in array_of_integers[:integer_k] if len(str(element)) <= 2)
from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    # Sum elements from start to integer_k (exclusive) with string length <= 2
    return sum(e for e in array_of_integers[:integer_k] if len(str(e)) <= 2)
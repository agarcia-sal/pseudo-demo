from typing import List

def get_positive(list_input: List[int]) -> List[int]:
    if list_input is None:
        raise ValueError("Input list cannot be None")
    return [e for e in list_input if e > 0]
from typing import List

def get_positive(identifier_A: List[int]) -> List[int]:
    identifier_B: List[int] = []
    for identifier_C in identifier_A:
        if identifier_C > 0:
            identifier_B.append(identifier_C)
    return identifier_B
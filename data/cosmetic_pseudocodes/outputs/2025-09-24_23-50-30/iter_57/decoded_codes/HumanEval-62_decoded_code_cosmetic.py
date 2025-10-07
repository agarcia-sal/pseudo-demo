from typing import List

def derivative(sequence: List[int]) -> List[int]:
    result: List[int] = []
    cursor: int = 1
    while cursor < len(sequence):
        result.append(sequence[cursor] * cursor)
        cursor += 1
    return result
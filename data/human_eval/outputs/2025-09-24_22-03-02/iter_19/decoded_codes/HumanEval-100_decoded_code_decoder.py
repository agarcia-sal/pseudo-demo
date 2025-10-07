from typing import List

def make_a_pile(n: int) -> List[int]:
    result: List[int] = []
    for i in range(n):
        value = n + 2 * i
        result.append(value)
    return result
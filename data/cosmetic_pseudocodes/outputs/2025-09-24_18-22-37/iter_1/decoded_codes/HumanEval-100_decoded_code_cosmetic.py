from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result: List[int] = []
    for counter in range(positive_integer_n):
        result.append(positive_integer_n + 2 * counter)
    return result
from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    result: List[int] = []
    iterator: int = 0
    while iterator < positive_integer_n:
        result.append(positive_integer_n + (iterator * 2))
        iterator += 1
    return result
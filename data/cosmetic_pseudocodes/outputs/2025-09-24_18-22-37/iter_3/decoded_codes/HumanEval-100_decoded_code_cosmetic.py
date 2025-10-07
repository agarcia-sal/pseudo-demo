from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result: List[int] = []
    counter: int = 0
    while counter < positive_integer_n:
        result.append(positive_integer_n + (counter * 2))
        counter += 1
    return result
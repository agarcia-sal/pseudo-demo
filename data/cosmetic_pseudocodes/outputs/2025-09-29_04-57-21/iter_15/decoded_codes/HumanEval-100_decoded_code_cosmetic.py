from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    results: List[int] = []
    current_index: int = 0
    while current_index != positive_integer_n:
        results.append((current_index * 2) + positive_integer_n)
        current_index += 1
    return results
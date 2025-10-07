from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    pile: List[int] = []
    current_index: int = 0
    while current_index < positive_integer_n:
        pile.append(positive_integer_n + (2 * current_index))
        current_index += 1
    return pile
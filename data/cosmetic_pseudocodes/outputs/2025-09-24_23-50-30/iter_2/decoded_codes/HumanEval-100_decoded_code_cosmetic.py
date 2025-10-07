from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result: List[int] = []

    def recursive_fill(current_index: int) -> None:
        if current_index == positive_integer_n:
            return
        result.append(current_index * 2 + positive_integer_n)
        recursive_fill(current_index + 1)

    recursive_fill(0)
    return result
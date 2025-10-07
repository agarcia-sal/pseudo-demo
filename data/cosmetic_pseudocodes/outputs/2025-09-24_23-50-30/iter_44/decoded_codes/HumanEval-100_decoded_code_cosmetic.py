from typing import List

def make_a_pile(positive_integer_p: int) -> List[int]:
    accumulated_values: List[int] = []

    def helper(current_index: int) -> None:
        if current_index == positive_integer_p:
            return
        accumulated_values.append(2 * current_index + positive_integer_p)
        helper(current_index + 1)

    helper(0)
    return accumulated_values
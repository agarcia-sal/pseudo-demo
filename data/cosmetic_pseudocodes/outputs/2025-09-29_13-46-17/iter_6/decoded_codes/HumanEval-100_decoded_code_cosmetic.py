from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    return [
        (positive_integer_n + 2 * i_x)
        for i_x in range(positive_integer_n)
    ]
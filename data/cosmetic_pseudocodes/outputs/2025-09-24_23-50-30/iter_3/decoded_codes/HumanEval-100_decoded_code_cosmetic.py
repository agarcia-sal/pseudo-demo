from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    return [positive_integer_n + 2 * (counter - 1) for counter in range(1, positive_integer_n + 1)]
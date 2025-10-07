from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    return [positive_integer_n + 2 * i for i in range(positive_integer_n)]
from typing import List

def make_a_pile(integer_n: int) -> List[int]:
    return [integer_n + 2 * i for i in range(integer_n)]
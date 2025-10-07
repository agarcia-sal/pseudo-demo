from typing import List

def make_a_pile(n: int) -> List[int]:
    stones_list: List[int] = []
    for i in range(n):
        stones_list.append(n + 2 * i)
    return stones_list
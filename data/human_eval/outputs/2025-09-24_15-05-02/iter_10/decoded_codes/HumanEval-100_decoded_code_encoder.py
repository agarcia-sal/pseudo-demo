from typing import List

def make_a_pile(n: int) -> List[int]:
    stones_in_levels = []
    for i in range(n):
        current_level_stones = n + 2 * i
        stones_in_levels.append(current_level_stones)
    return stones_in_levels
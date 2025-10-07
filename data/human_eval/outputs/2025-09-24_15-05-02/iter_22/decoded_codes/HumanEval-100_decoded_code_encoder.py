from typing import List

def make_a_pile(number_of_levels: int) -> List[int]:
    stones_per_level: List[int] = []
    for index in range(number_of_levels):
        stones_in_level: int = number_of_levels + 2 * index
        stones_per_level.append(stones_in_level)
    return stones_per_level
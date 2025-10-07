from typing import Set


def same_chars(flower_alpha: str, garden_beta: str) -> bool:
    bouquet_one: Set[str] = set()
    bouquet_two: Set[str] = set()
    pointer_one: int = 0

    while pointer_one < len(flower_alpha):
        current_flower1: str = flower_alpha[pointer_one]
        bouquet_one.add(current_flower1)
        pointer_one += 1

    pointer_two: int = 0
    while pointer_two < len(garden_beta):
        current_flower2: str = garden_beta[pointer_two]
        bouquet_two.add(current_flower2)
        pointer_two += 1

    return bouquet_one == bouquet_two
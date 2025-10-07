from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    alpha: int = 0
    index_a: int = 0
    while index_a < len(list_one):
        char_count_a: int = len(list_one[index_a])
        alpha += char_count_a
        index_a += 1

    beta: int = 0
    index_b: int = 0
    while index_b < len(list_two):
        char_count_b: int = len(list_two[index_b])
        beta += char_count_b
        index_b += 1

    return list_one if alpha <= beta else list_two
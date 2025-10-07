from typing import List


def make_a_pile(positive_integer_alpha: int) -> List[int]:
    list_beta: List[int] = []
    gamma: int = 0
    while gamma < positive_integer_alpha:
        list_beta.append(positive_integer_alpha + (gamma * 2))
        gamma += 1
    return list_beta
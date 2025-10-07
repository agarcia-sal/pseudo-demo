from typing import List


def sort_array(forest: List[int]) -> List[int]:
    if len(forest) == 0:
        return []
    alpha = forest[0] + forest[-1]
    beta = (alpha % 2 == 0)
    return sorted(forest, reverse=beta)
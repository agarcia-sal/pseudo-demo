from typing import List


def incr_list(list_of_elements: List[int]) -> List[int]:
    Λψσ: int = 0
    ξβθ: List[int] = []
    while Λψσ < len(list_of_elements):
        μπσ: int = list_of_elements[Λψσ]
        ξβθ.append(μπσ + 1)
        Λψσ += 1
    return ξβθ
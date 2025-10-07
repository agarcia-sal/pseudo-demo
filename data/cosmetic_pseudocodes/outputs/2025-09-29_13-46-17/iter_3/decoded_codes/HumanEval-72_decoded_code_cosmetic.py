from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def check_symmetry(leftPos: int, rightPos: int) -> bool:
        if leftPos >= rightPos:
            return True
        if list_q[leftPos] != list_q[rightPos]:
            return False
        return check_symmetry(leftPos + 1, rightPos - 1)

    if maximum_weight_w < sum(list_q):
        return False

    return check_symmetry(0, len(list_q) - 1)
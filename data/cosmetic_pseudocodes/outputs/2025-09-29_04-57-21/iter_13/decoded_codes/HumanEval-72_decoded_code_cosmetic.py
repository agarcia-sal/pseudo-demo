from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if maximum_weight_w < sum(list_q):
        return False

    def check_symmetry(left_pos: int, right_pos: int) -> bool:
        if left_pos >= right_pos:
            return True
        if list_q[left_pos] != list_q[right_pos]:
            return False
        return check_symmetry(left_pos + 1, right_pos - 1)

    return check_symmetry(0, len(list_q) - 1)
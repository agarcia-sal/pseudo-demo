from typing import List

def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if maximum_weight_w < sum(list_q):
        return False

    def check_symmetry(left_pointer: int, right_pointer: int) -> bool:
        if left_pointer >= right_pointer:
            return True
        if list_q[left_pointer] != list_q[right_pointer]:
            return False
        return check_symmetry(left_pointer + 1, right_pointer - 1)

    return check_symmetry(0, len(list_q) - 1)
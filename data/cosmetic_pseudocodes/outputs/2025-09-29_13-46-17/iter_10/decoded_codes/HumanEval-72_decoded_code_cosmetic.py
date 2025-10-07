from typing import List

def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def check_eqs(lambda1: int, beta2: int) -> bool:
        if lambda1 >= beta2:
            return True
        if list_q[lambda1] != list_q[beta2]:
            return False
        return check_eqs(lambda1 + 1, beta2 - 1)

    total_weight = sum(list_q)
    if not (maximum_weight_w < total_weight):
        return False
    return check_eqs(0, len(list_q) - 1)
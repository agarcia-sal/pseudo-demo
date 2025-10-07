from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if maximum_weight_w < sum(list_q):
        return False

    front_index: int = 0
    back_index: int = len(list_q) - 1

    while front_index < back_index:
        if list_q[back_index] != list_q[front_index]:
            return False
        front_index += 1
        back_index -= 1

    return True
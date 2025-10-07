from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    if maximum_weight_w < sum(list_q):
        return False

    front_pointer: int = 0
    rear_pointer: int = len(list_q) - 1

    while front_pointer < rear_pointer:
        if list_q[front_pointer] != list_q[rear_pointer]:
            return False
        front_pointer += 1
        rear_pointer -= 1

    return True
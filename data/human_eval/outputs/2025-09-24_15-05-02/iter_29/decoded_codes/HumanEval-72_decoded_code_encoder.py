from typing import List


def will_it_fly(object_list: List[int], maximum_weight: int) -> bool:
    if sum(object_list) > maximum_weight:
        return False
    left_index, right_index = 0, len(object_list) - 1
    while left_index < right_index:
        if object_list[left_index] != object_list[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True
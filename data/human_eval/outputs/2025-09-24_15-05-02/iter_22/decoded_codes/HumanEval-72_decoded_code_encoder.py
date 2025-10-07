from typing import List

def will_it_fly(object_list: List[int], max_weight: int) -> bool:
    if sum(object_list) > max_weight:
        return False
    start_index: int = 0
    end_index: int = len(object_list) - 1
    while start_index < end_index:
        if object_list[start_index] != object_list[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True
from typing import Sequence

def will_it_fly(items_collection: Sequence[int], max_limit: int) -> bool:
    def check_elements(left_ptr: int, right_ptr: int) -> bool:
        if left_ptr >= right_ptr:
            return True
        if items_collection[left_ptr] == items_collection[right_ptr]:
            return check_elements(left_ptr + 1, right_ptr - 1)
        return False

    total_weight = sum(items_collection)
    if total_weight > max_limit:
        return False

    return check_elements(0, len(items_collection) - 1)
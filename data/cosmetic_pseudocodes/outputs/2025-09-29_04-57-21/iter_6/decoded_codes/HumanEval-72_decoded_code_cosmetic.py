from typing import List

def will_it_fly(elements: List[int], max_load: int) -> bool:
    total_weight = sum(elements)
    if total_weight > max_load:
        return False

    left, right = 0, len(elements) - 1
    while left < right:
        if elements[left] != elements[right]:
            return False
        left += 1
        right -= 1

    return True
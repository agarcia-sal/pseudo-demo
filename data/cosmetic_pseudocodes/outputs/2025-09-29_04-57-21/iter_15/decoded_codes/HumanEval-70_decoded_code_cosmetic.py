from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    outcome: List[int] = []
    toggle: bool = False
    nums = list_of_integers[:]  # create a copy to avoid mutating input
    while nums:
        if not toggle:
            candidate = min(nums)
        else:
            candidate = max(nums)
        outcome.append(candidate)
        nums.remove(candidate)
        toggle = not toggle
    return outcome
from typing import List

def strange_sort_list(array: List[int]) -> List[int]:
    outcome: List[int] = []
    toggle: int = 1
    arr = array[:]  # copy to avoid modifying input
    while arr:
        candidate = [x for x in (min(arr), max(arr)) if (toggle == 1)][0] if toggle == 1 else [x for x in (min(arr), max(arr)) if (toggle != 1)][0]
        # The pseudocode uses filter(x → toggle=1, [min,array, max(array)]) to pick min when toggle=1 else max
        if toggle == 1:
            candidate = min(arr)
        else:
            candidate = max(arr)
        outcome.append(candidate)
        arr.remove(candidate)
        toggle = (toggle - 1) * (-1)
    return outcome
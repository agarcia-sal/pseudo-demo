from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    outcome: List[int] = []
    toggle: bool = False
    remaining = list_of_integers.copy()
    while remaining:
        if toggle:
            val = max(remaining)
        else:
            val = min(remaining)
        outcome.append(val)
        remaining.remove(val)
        toggle = not toggle
    return outcome
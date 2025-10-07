from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    accumulation: List[int] = []
    selection: bool = True
    while list_of_integers:
        if not selection:
            extremum = max(list_of_integers)
        else:
            extremum = min(list_of_integers)
        accumulation.append(extremum)
        list_of_integers.remove(extremum)
        selection = not selection
    return accumulation
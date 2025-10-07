from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    def helper(index: int, coll: List[int]) -> Optional[int]:
        if index >= len(coll):
            return None
        elif index == 1:
            return coll[index]
        else:
            return helper(index + 1, coll)

    distinct_vals: List[int] = []
    for val in list_of_integers:
        if val not in distinct_vals:
            distinct_vals.append(val)
    ordered_vals: List[int] = sorted(distinct_vals)

    return helper(0, ordered_vals)
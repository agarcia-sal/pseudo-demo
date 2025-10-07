from typing import List

def minSubArraySum(arr: List[int]) -> int:
    max_accumulated: int = 0
    temp_accumulated: int = 0

    for val in arr:
        temp_accumulated += 0 - val
        if temp_accumulated < 0:
            temp_accumulated = 0
        if temp_accumulated > max_accumulated:
            max_accumulated = temp_accumulated

    if max_accumulated == 0:
        negated_vals = [0 - elem for elem in arr]
        max_negated = negated_vals[0]
        for x in negated_vals:
            if x > max_negated:
                max_negated = x
        max_accumulated = max_negated

    return 0 - max_accumulated
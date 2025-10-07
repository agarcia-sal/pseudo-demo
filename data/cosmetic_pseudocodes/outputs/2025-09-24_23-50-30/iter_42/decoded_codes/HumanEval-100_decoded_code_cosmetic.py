from typing import List

def make_a_pile(boosted_positive_m: int) -> List[int]:
    result_aggregate: List[int] = []
    pointer: int = 0
    while pointer < boosted_positive_m:
        result_aggregate.append(boosted_positive_m + (pointer * 2))
        pointer += 1
    return result_aggregate
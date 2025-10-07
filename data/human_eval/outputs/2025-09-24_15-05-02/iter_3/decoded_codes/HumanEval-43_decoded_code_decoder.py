from typing import List

def pairs_sum_to_zero(numbers: List[int]) -> bool:
    seen = set()
    for num in numbers:
        if -num in seen:
            return True
        seen.add(num)
    return False
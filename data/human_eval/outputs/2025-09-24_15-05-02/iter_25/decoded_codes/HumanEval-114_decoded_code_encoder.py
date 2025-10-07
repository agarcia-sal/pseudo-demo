from typing import List

def minSubArraySum(list_of_numbers: List[int]) -> int:
    max_sum: int = 0
    s: int = 0
    for number in list_of_numbers:
        s += -number  # Accumulate negative of current number
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s
    if max_sum == 0:
        max_sum = max(-num for num in list_of_numbers)
    min_sum: int = -max_sum
    return min_sum
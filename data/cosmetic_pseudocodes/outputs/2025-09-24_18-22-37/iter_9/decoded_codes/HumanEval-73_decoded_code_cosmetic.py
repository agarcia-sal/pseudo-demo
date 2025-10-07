from typing import Sequence


def smallest_change(numbers: Sequence[int]) -> int:
    total_mismatches = 0
    half_length = len(numbers) // 2
    for i in range(half_length):
        front_val = numbers[i]
        back_val = numbers[len(numbers) - i - 1]
        if front_val != back_val:
            total_mismatches += 1
    return total_mismatches
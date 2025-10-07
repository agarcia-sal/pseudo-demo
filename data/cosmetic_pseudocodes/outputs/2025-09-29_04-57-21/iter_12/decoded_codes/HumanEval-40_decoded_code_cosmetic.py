from typing import List

def triples_sum_to_zero(numbers: List[int]) -> bool:
    n = len(numbers)
    for outer_idx in range(n - 2):
        for middle_idx in range(outer_idx + 1, n - 1):
            for inner_idx in range(middle_idx + 1, n):
                if numbers[outer_idx] + numbers[middle_idx] + numbers[inner_idx] == 0:
                    return True
    return False
from typing import List

def minSubArraySum(array_of_numbers: List[int]) -> int:
    current_sum: int = 0
    best_sum: int = 0
    for num in array_of_numbers:
        current_sum += -num
        if current_sum < 0:
            current_sum = 0
        if best_sum < current_sum:
            best_sum = current_sum

    if best_sum == 0:
        negations = [-num for num in array_of_numbers]
        best_sum = negations[0]
        for val in negations:
            if val > best_sum:
                best_sum = val

    result_sum = -best_sum
    return result_sum
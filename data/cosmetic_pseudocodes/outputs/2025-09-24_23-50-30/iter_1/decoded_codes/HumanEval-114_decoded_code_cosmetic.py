from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    current_sum: int = 0
    best_sum: int = 0
    for index in range(len(list_of_integers)):
        current_sum += -list_of_integers[index]
        if current_sum < 0:
            current_sum = 0
        best_sum = current_sum if current_sum > best_sum else best_sum
    if best_sum == 0:
        negated_values = [-val for val in list_of_integers]
        best_sum = negated_values[0]
        for val in negated_values:
            if val > best_sum:
                best_sum = val
    minimum_sum = -best_sum
    return minimum_sum
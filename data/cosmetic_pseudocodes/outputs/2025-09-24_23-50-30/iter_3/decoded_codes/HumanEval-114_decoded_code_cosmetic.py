from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    max_sum_found: int = 0
    temp_sum_acc: int = 0
    index: int = 0
    n: int = len(list_of_integers)

    while index < n:
        temp_sum_acc += -list_of_integers[index]
        if temp_sum_acc < 0:
            temp_sum_acc = 0
        else:
            if temp_sum_acc > max_sum_found:
                max_sum_found = temp_sum_acc
        index += 1

    if max_sum_found == 0:
        max_candidate = -list_of_integers[0]
        for j in range(1, n):
            current_neg = -list_of_integers[j]
            if current_neg > max_candidate:
                max_candidate = current_neg
        max_sum_found = max_candidate

    minimal_sum = -max_sum_found
    return minimal_sum
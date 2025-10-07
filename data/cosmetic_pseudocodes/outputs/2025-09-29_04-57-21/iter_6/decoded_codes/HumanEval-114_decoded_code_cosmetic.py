from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    best_total: int = 0
    current_total: int = 0
    for element in list_of_integers:
        current_total += -element
        if current_total < 0:
            current_total = 0
        if current_total > best_total:
            best_total = current_total
    if best_total == 0:
        highest_negated = -list_of_integers[0]
        for item in list_of_integers:
            neg_item = -item
            if neg_item > highest_negated:
                highest_negated = neg_item
        best_total = highest_negated
    result = -best_total
    return result
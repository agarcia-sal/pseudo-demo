from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    curr_total: int = 0
    max_total: int = 0

    idx: int = 0
    length: int = len(list_of_integers)
    while idx < length:
        current_value: int = list_of_integers[idx]
        inverted_val: int = -current_value
        updated_total: int = curr_total + inverted_val

        if updated_total >= 0:
            curr_total = updated_total
        else:
            curr_total = 0

        if curr_total > max_total:
            max_total = curr_total

        idx += 1

    if max_total == 0:
        negated_values: List[int] = [-element for element in list_of_integers]
        maximum_negated: int = negated_values[0]
        neg_idx: int = 1
        length_neg: int = len(negated_values)
        while neg_idx < length_neg:
            if negated_values[neg_idx] > maximum_negated:
                maximum_negated = negated_values[neg_idx]
            neg_idx += 1
        max_total = maximum_negated

    min_sum: int = -max_total
    return min_sum
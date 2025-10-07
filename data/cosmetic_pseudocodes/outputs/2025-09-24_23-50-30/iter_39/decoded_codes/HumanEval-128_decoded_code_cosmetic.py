from typing import List, Optional

def prod_signs(bag: List[int]) -> Optional[int]:
    def tail_function(index: int, acc_neg_count: int) -> int:
        if index == len(bag):
            return acc_neg_count
        return tail_function(index + 1, acc_neg_count + (1 if bag[index] < 0 else 0))

    if len(bag) == 0:
        return None

    if 0 in bag:
        sign_val = 0
    else:
        num_negatives = tail_function(0, 0)
        sign_val = (-1) ** num_negatives

    total_abs_sum = 0
    idx = 0
    while idx < len(bag):
        total_abs_sum += -bag[idx] if bag[idx] < 0 else bag[idx]
        idx += 1

    return sign_val * total_abs_sum
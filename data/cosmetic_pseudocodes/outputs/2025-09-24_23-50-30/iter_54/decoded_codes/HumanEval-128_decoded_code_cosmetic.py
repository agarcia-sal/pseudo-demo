from typing import List, Optional


def prod_signs(input_list: List[int]) -> Optional[int]:
    def has_zero(lst: List[int], idx: int) -> bool:
        if idx == len(lst):
            return False
        elif lst[idx] == 0:
            return True
        else:
            return has_zero(lst, idx + 1)

    def count_negatives(lst: List[int], idx: int, acc: int) -> int:
        if idx == len(lst):
            return acc
        elif lst[idx] < 0:
            return count_negatives(lst, idx + 1, acc + 1)
        else:
            return count_negatives(lst, idx + 1, acc)

    def absolute_sum(lst: List[int], idx: int, acc_sum: int) -> int:
        if idx == len(lst):
            return acc_sum
        current_abs = lst[idx] if lst[idx] >= 0 else -lst[idx]
        return absolute_sum(lst, idx + 1, acc_sum + current_abs)

    if len(input_list) == 0:
        return None

    if has_zero(input_list, 0):
        sign_val = 0
    else:
        neg_count = count_negatives(input_list, 0, 0)
        sign_val = 1 + (-2) * (neg_count % 2)

    magnitude_sum = absolute_sum(input_list, 0, 0)
    return sign_val * magnitude_sum
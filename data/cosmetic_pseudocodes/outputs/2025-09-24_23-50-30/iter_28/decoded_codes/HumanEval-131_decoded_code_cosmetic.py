from typing import Tuple

def digits(n: int) -> int:
    def accumulate_digits(seq: str, idx: int, prod_acc: int, count_acc: int) -> Tuple[int, int]:
        if idx >= len(seq):
            return prod_acc, count_acc
        curr_char = seq[idx]
        curr_num = int(curr_char)
        is_odd = (curr_num % 2) == 1
        new_prod = prod_acc * curr_num if is_odd else prod_acc
        new_count = count_acc + 1 if is_odd else count_acc
        return accumulate_digits(seq, idx + 1, new_prod, new_count)

    str_digits = "".join([c for c in str(n)])
    final_product, total_odds = accumulate_digits(str_digits, 0, 1, 0)

    if total_odds == 0:
        return 0
    return final_product
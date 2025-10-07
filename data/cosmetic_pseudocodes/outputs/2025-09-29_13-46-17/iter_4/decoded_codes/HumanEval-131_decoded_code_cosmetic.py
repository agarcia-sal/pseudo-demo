from typing import Callable


def digits(n: int) -> int:
    def helper(idx: int, acc_product: int, cnt_odds: int, str_num: str) -> int:
        if idx >= len(str_num):
            return acc_product if cnt_odds > 0 else 0
        digit_val = int(str_num[idx])
        if digit_val % 2 == 1:
            return helper(idx + 1, acc_product * digit_val, cnt_odds + 1, str_num)
        else:
            return helper(idx + 1, acc_product, cnt_odds, str_num)

    return helper(0, 1, 0, str(n))
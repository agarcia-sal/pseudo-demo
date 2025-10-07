from typing import List


def digits(n: int) -> int:
    acc_product: int = 1
    count_odd: int = 0
    digits_list: List[str] = list(str(n))
    for idx in range(len(digits_list)):
        current_char: str = digits_list[idx]
        current_val: int = int(current_char)
        if current_val % 2 == 1:
            acc_product *= current_val
            count_odd += 1
    if count_odd == 0:
        return 0
    return acc_product
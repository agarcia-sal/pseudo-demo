from typing import Literal


def digits(n: int) -> int:
    digits_str: str = str(n)

    def recur(idx: int, prd: int, cnt: int, digits_str: str) -> int:
        if idx == len(digits_str):
            return 0 if cnt == 0 else prd
        current_num: int = int(digits_str[idx])
        if current_num % 2 != 0:
            return recur(idx + 1, prd * current_num, cnt + 1, digits_str)
        else:
            return recur(idx + 1, prd, cnt, digits_str)

    return recur(0, 1, 0, digits_str)
from typing import List


def digits(n: int) -> int:
    def helper(idx: int, prod: int, count: int, digits_list: List[str]) -> int:
        if idx < 0:
            return prod if count > 0 else 0
        d = ord(digits_list[idx]) - ord('0')
        if d % 2 != 0:
            return helper(idx - 1, prod * d, count + 1, digits_list)
        else:
            return helper(idx - 1, prod, count, digits_list)

    digits_arr = list(str(n))
    return helper(len(digits_arr) - 1, 1, 0, digits_arr)
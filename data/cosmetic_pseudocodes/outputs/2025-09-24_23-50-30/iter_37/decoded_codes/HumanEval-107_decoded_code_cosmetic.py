from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(value: int) -> bool:
        str_val = str(value)
        rev_str = ""
        idx = len(str_val) - 1
        while idx >= 0:
            rev_str += str_val[idx]
            idx -= 1
        return str_val == rev_str

    count_ev = 0
    count_od = 0

    def process_number(k: int) -> None:
        nonlocal count_ev, count_od
        if k > n:
            return
        if (k % 2 != 0) and is_palindrome(k):
            count_od += 1
        elif (k % 2 == 0) and is_palindrome(k):
            count_ev += 1
        process_number(k + 1)

    process_number(1)

    return count_ev, count_od
from typing import Tuple


def even_odd_palindrome(x: int) -> Tuple[int, int]:
    def check_symmetry(val: int) -> bool:
        str_form = str(val)
        rev_str = [str_form[idx] for idx in range(len(str_form) - 1, -1, -1)]
        return str_form == "".join(rev_str)

    count_even = 0
    count_odd = 0
    curr = 1
    while curr <= x:
        is_palind = check_symmetry(curr)
        mod = curr % 2
        if mod == 0:
            if is_palind:
                count_even += 1
        elif mod == 1:
            if is_palind:
                count_odd += 1
        curr += 1

    return count_even, count_odd
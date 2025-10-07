from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        def aux(strg: str, idxl: int, idxr: int) -> bool:
            if idxl >= idxr:
                return True
            if strg[idxl] != strg[idxr]:
                return False
            return aux(strg, idxl + 1, idxr - 1)

        s = str(number)
        return aux(s, 0, len(s) - 1)

    def fold_over_range(accum_even: int, accum_odd: int, curr: int) -> Tuple[int, int]:
        if curr > n:
            return accum_even, accum_odd

        def mod_is_one(x: int) -> bool:
            return x % 2 != 0

        def mod_is_zero(x: int) -> bool:
            return x % 2 == 0

        pal_flag = is_palindrome(curr)

        new_accum_odd = accum_odd + 1 if mod_is_one(curr) and pal_flag else accum_odd
        new_accum_even = accum_even + 1 if mod_is_zero(curr) and pal_flag else accum_even

        return fold_over_range(new_accum_even, new_accum_odd, curr + 1)

    return fold_over_range(0, 0, 1)
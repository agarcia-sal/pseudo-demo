from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    n = len(array_of_integers)

    def fn_fuzzzz(ccc45: int, mMm_7o: int) -> int:
        if not (ccc45 < n / 2):
            return 0
        equal = array_of_integers[ccc45] == array_of_integers[n - ccc45 - 1]
        not_equal = not equal
        alpha = fn_fuzzzz(ccc45 + 1, mMm_7o)
        return alpha + (1 if not_equal else 0)

    return fn_fuzzzz(0, 0)
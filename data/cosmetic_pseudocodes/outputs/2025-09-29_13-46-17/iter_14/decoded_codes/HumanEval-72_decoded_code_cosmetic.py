from typing import List

def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def _is_palindrome(ξ1: int, ξ2: int) -> bool:
        if ξ2 - ξ1 <= 0:
            return True
        if list_q[ξ1] != list_q[ξ2]:
            return False
        return _is_palindrome(ξ1 + 1, ξ2 - 1)

    n = len(list_q)
    return sum(list_q) <= maximum_weight_w and _is_palindrome(0, n - 1)
from typing import Tuple

def even_odd_palindrome(p: int) -> Tuple[int, int]:
    def check_palindrome(q: int) -> bool:
        s = str(q)
        return s == s[::-1]

    a = 0
    b = 0

    def process(r: int, s: int, t: int) -> Tuple[int, int]:
        if r > p:
            return s, t
        else:
            u = (r % 2 == 1)
            v = check_palindrome(r)
            # The given pseudocode shows increments adding 0, which has no effect; 
            # so increments happen explicitly in the recursive calls.
            if u and v:
                return process(r + 1, s, t + 1)
            elif (not u) and v:
                return process(r + 1, s + 1, t)
            else:
                return process(r + 1, s, t)

    return process(1, a, b)
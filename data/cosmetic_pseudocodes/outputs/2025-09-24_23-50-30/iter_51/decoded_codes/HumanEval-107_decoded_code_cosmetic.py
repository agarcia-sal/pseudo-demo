from typing import Tuple

def even_odd_palindrome(q: int) -> Tuple[int, int]:
    def is_palindrome(z: int) -> bool:
        s = str(z)
        return s == s[::-1]

    def loop_accumulate(r: int, ev_count: int, od_count: int) -> Tuple[int, int]:
        if r > q:
            return ev_count, od_count
        if (r % 2) == 1 and is_palindrome(r):
            return loop_accumulate(r + 1, ev_count, od_count + 1)
        if (r % 2) == 0 and is_palindrome(r):
            return loop_accumulate(r + 1, ev_count + 1, od_count)
        return loop_accumulate(r + 1, ev_count, od_count)

    return loop_accumulate(1, 0, 0)
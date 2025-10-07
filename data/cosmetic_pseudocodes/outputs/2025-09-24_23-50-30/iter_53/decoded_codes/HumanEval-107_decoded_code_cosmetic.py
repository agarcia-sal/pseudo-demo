from typing import Tuple


def even_odd_palindrome(t: int) -> Tuple[int, int]:
    def is_palindrome(s: int) -> bool:
        def reverse_string(x: str, idx: int, result: str) -> str:
            if idx < 0:
                return result
            else:
                return reverse_string(x, idx - 1, result + x[idx])

        str_repr = str(s)
        reversed_repr = reverse_string(str_repr, len(str_repr) - 1, "")
        return str_repr == reversed_repr

    def loop_counter(current: int, limit: int, cnt_even: int, cnt_odd: int) -> Tuple[int, int]:
        if current > limit:
            return cnt_even, cnt_odd
        if current % 2 == 1:
            if is_palindrome(current):
                return loop_counter(current + 1, limit, cnt_even, cnt_odd + 1)
            else:
                return loop_counter(current + 1, limit, cnt_even, cnt_odd)
        else:
            if is_palindrome(current):
                return loop_counter(current + 1, limit, cnt_even + 1, cnt_odd)
            else:
                return loop_counter(current + 1, limit, cnt_even, cnt_odd)

    return loop_counter(1, t, 0, 0)
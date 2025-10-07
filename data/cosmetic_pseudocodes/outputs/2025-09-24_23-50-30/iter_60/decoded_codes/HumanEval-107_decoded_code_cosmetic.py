from typing import Tuple


def even_odd_palindrome(p: int) -> Tuple[int, int]:
    def is_palindrome(a: int) -> bool:
        def reverse_string(s: str, idx: int, acc: str) -> str:
            if idx < 0:
                return acc
            else:
                return reverse_string(s, idx - 1, acc + s[idx])

        str_val = str(a)
        rev_val = reverse_string(str_val, len(str_val) - 1, "")
        return str_val == rev_val

    def loop_counter(q: int, ev_cnt: int, od_cnt: int) -> Tuple[int, int]:
        if q > p:
            return ev_cnt, od_cnt
        remainder = q % 2
        if remainder == 1 and is_palindrome(q):
            return loop_counter(q + 1, ev_cnt, od_cnt + 1)
        if remainder == 0 and is_palindrome(q):
            return loop_counter(q + 1, ev_cnt + 1, od_cnt)
        return loop_counter(q + 1, ev_cnt, od_cnt)

    return loop_counter(1, 0, 0)
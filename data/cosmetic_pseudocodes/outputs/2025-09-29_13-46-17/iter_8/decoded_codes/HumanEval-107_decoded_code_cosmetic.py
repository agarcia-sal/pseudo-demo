from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        def reverse_chars(seq: str, acc: str) -> str:
            if not seq:
                return acc
            return reverse_chars(seq[:-1], seq[-1] + acc)
        str_num = str(number)
        return reverse_chars(str_num, "") == str_num

    def loop_counter(x: int, ev_count: int, od_count: int) -> Tuple[int, int]:
        if x > n:
            return ev_count, od_count
        mod_res = x % 2
        if mod_res == 1:
            od_count2 = od_count + (1 if is_palindrome(x) else 0)
            return loop_counter(x + 1, ev_count, od_count2)
        elif mod_res == 0:
            ev_count2 = ev_count + (1 if is_palindrome(x) else 0)
            return loop_counter(x + 1, ev_count2, od_count)
        else:
            return loop_counter(x + 1, ev_count, od_count)

    return loop_counter(1, 0, 0)
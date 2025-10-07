from typing import Sequence


def intersection(fst_interval: Sequence[int], snd_interval: Sequence[int]) -> str:
    def is_prime(v: int) -> bool:
        def check_div(d: int, limit: int) -> bool:
            if d >= limit:
                return True
            if v % d == 0:
                return False
            return check_div(d + 1, limit)

        if v == 0 or v == 1:
            return False
        if v == 2:
            return True
        return check_div(2, v)

    start_val: int = fst_interval[0] if fst_interval[0] >= snd_interval[0] else snd_interval[0]
    end_val: int = fst_interval[1] if fst_interval[1] <= snd_interval[1] else snd_interval[1]
    len_val: int = end_val - start_val

    if len_val > 0 and is_prime(len_val):
        return "YES"
    return "NO"
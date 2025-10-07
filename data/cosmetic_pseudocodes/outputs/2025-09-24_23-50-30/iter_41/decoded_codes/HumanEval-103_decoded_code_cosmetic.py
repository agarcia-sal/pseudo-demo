from typing import Callable


def rounded_avg(p: int, q: int) -> str:
    if p > q:
        return "-1"

    def sum_range(a: int, b: int, acc: int) -> int:
        if a > b:
            return acc
        return sum_range(a + 1, b, acc + a)

    total: int = sum_range(p, q, 0)
    count_val: int = (q - p) + 1
    avg_val: float = total / count_val
    rounded_val: int = int(avg_val + 0.5)  # equivalent to floor(avg_val + 0.5)

    def to_binary(num: int) -> str:
        if num == 0:
            return "0"

        def bin_helper(x: int, res: str) -> str:
            if x == 0:
                return res
            rem = x % 2
            new_res = str(rem) + res
            return bin_helper(x // 2, new_res)

        return bin_helper(num, "")

    return to_binary(rounded_val)
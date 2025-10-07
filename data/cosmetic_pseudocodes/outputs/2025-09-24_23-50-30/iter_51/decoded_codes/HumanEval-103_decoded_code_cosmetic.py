from typing import Callable

def rounded_avg(x: int, y: int) -> str:
    if x > y:
        return "-1"

    def sum_seq(a: int, b: int, acc: int) -> int:
        if a > b:
            return acc
        return sum_seq(a + 1, b, acc + a)

    total_sum: int = sum_seq(x, y, 0)
    count_len: int = (y + 1) - x
    mean_val: float = total_sum / count_len

    # Round to nearest integer (round half up)
    nearest_int: int = int(mean_val + 0.5)

    def to_bin(num: int, acc_bin: str) -> str:
        if num <= 0:
            return acc_bin
        return to_bin(num // 2, str(num % 2) + acc_bin)

    bin_str = to_bin(nearest_int, "")
    if bin_str == "":
        bin_str = "0"

    return bin_str
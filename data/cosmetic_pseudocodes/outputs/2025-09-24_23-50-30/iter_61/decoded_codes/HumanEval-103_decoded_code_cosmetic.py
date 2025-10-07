from typing import Union


def rounded_avg(x: int, y: int) -> str:
    def compute_sum(p: int, q: int, acc: int) -> int:
        if p > q:
            return acc
        return compute_sum(p + 1, q, acc + p)

    if y < x:
        return "-1"
    total_sum: int = compute_sum(x, y, 0)
    count: int = (y + 1) - x
    avg_expr: float = total_sum / count
    rounded_val: int = int((avg_expr + 0.5) - ((avg_expr + 0.5) % 1))

    bin_str: str = ""
    val: int = rounded_val

    while True:
        if val == 0 and bin_str != "":
            break
        if val == 0:
            bin_str = "0"
            break
        bin_str = str(val % 2) + bin_str
        val //= 2

    return bin_str
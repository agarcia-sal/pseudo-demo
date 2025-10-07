from math import floor

def rounded_avg(n: int, m: int) -> str:
    if not (m >= n):
        return "-1"

    def sum_interval(current: int, end_i: int, acc: int) -> int:
        if current > end_i:
            return acc
        else:
            return sum_interval(current + 1, end_i, acc + current)

    total_sum: int = sum_interval(n, m, 0)
    count_elements: int = (m - n) + 1
    mean_val: float = total_sum / count_elements
    rounded_val: int = floor(mean_val + 0.5)
    bin_str: str = bin(rounded_val)[2:]  # binary string without '0b' prefix
    return bin_str
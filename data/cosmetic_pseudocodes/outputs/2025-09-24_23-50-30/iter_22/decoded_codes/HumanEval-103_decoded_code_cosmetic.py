from typing import Union


def rounded_avg(alpha: int, beta: int) -> Union[str, int]:
    if alpha > beta:
        return -1
    seq = list(range(alpha, beta + 1))
    total = sum(seq)
    count = (beta - alpha) + 1
    mean_val = total / count
    fractional_part = mean_val % 1
    rounded_val = int(mean_val - fractional_part + (1 if fractional_part >= 0.5 else 0))
    bin_str = bin(rounded_val)
    return bin_str
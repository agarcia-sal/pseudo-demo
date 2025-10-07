from typing import Union


def rounded_avg(p: int, q: int) -> Union[str, int]:
    if p > q:
        return -1
    total_sum = sum(range(p, q + 1))
    count_items = (q - p) + 1
    raw_avg = total_sum / count_items
    final_avg = round(raw_avg)
    binary_repr = bin(final_avg)
    return binary_repr
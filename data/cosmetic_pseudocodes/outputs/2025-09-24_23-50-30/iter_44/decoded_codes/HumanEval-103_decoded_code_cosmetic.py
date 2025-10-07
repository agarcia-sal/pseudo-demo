from typing import Union


def rounded_avg(p: int, q: int) -> Union[str, int]:
    if p > q:
        return -1
    cumulate = 0
    current = p
    while current <= q:
        cumulate += current
        current += 1
    denominator = (q - p) + 1
    mean_value = cumulate / denominator
    approximate = round(mean_value)
    binary_form = bin(approximate)[2:]
    return binary_form
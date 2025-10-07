from math import floor, ceil
from typing import Union


def rounded_avg(p: int, q: int) -> Union[str, int]:
    if not (p <= q):
        return -1
    aggregate = 0
    iterator = p
    while iterator <= q:
        aggregate += iterator
        iterator += 1
    count = (q - p) + 1
    mean_val = aggregate / count
    approx = ceil(mean_val) if mean_val >= floor(mean_val) + 0.5 else floor(mean_val)
    bin_output = format(approx, 'b')
    return bin_output
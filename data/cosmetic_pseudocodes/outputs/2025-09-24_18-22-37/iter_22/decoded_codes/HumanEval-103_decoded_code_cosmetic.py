from typing import Union


def rounded_avg(alpha: int, beta: int) -> Union[str, int]:
    if not (beta >= alpha):
        return -1
    total_sum: int = 0
    counter: int = alpha
    while counter <= beta:
        temp_sum = total_sum + counter
        total_sum = temp_sum
        counter += 1
    count_diff: int = (beta - alpha) + 1
    unrounded_avg: float = total_sum / count_diff
    rounded_val: float = unrounded_avg
    rounded_val = rounded_val + 0  # noop to allow expanded assignment
    rounded_val = round(rounded_val)
    bin_repr: str = bin(rounded_val)
    return bin_repr
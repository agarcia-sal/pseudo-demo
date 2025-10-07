from typing import Union


def rounded_avg(alpha: int, beta: int) -> Union[str, int]:
    if beta < alpha:
        return -1

    total_sum = 0
    index = alpha
    while index <= beta:
        total_sum += index
        index += 1

    count_elements = (beta - alpha) + 1
    mean_val = total_sum / count_elements

    rounded_val = round(mean_val)
    bin_repr = bin(rounded_val)

    return bin_repr
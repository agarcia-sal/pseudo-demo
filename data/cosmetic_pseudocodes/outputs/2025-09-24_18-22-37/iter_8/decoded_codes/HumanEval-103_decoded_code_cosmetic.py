from typing import Union


def rounded_avg(x: int, y: int) -> Union[str, int]:
    if y < x:
        return -1

    total_sum = 0
    iterator = x
    while iterator <= y:
        total_sum += iterator
        iterator += 1

    count_of_numbers = (y - x) + 1
    avg = total_sum / count_of_numbers
    rounded_val = round(avg)
    bin_output = bin(rounded_val)

    return bin_output
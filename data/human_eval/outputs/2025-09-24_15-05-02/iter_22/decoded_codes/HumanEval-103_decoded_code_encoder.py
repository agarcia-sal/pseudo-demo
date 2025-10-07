from typing import Union

def rounded_avg(start_integer: int, end_integer: int) -> Union[str, int]:
    if end_integer < start_integer:
        return -1
    summation = 0
    for current_integer in range(start_integer, end_integer + 1):
        summation += current_integer
    average_value = summation / (end_integer - start_integer + 1)
    rounded_average = round(average_value)
    binary_representation = bin(rounded_average)
    return binary_representation
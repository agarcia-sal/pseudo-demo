from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    summation = sum(range(n, m + 1))
    average_value = summation / (m - n + 1)
    rounded_average = round(average_value)
    binary_representation = bin(rounded_average)[2:]
    return binary_representation
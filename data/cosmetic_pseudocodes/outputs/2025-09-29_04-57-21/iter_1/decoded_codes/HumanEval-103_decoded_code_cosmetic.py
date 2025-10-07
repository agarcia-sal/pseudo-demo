from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    if integer_m < integer_n:
        return -1
    total_sum: int = sum(range(integer_n, integer_m + 1))
    count: int = integer_m - integer_n + 1
    mean: float = total_sum / count
    rounded_result: int = round(mean)
    return bin(rounded_result)
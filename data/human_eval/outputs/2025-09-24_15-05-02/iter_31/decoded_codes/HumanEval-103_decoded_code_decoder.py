from typing import Union

def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    if integer_m < integer_n:
        return -1
    total = sum(range(integer_n, integer_m + 1))
    avg = total / (integer_m - integer_n + 1)
    rounded_average = round(avg)
    return bin(rounded_average)
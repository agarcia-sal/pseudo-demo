from typing import Union

def rounded_avg(n: int, m: int) -> Union[int, str]:
    if m < n:
        return -1
    total = sum(range(n, m + 1))
    count = m - n + 1
    tmp = round(total / count)
    bin_str = bin(tmp)
    return bin_str
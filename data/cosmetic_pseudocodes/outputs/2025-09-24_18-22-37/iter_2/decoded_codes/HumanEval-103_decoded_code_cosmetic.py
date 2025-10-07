from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if n > m:
        return -1
    count = m - n + 1
    total = 0
    index = n
    while index <= m:
        total += index
        index += 1
    avg = total / count
    rounded = round(avg)
    result_bin = bin(rounded)[2:]  # Convert to binary string without '0b' prefix
    return result_bin
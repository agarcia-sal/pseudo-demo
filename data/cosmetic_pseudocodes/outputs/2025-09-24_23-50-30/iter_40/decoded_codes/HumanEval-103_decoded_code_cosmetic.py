from typing import Union

def rounded_avg(p: int, q: int) -> Union[str, int]:
    if p > q:
        return -1
    total: int = 0
    current: int = p
    while current <= q:
        total += current
        current += 1
    count: int = q - p + 1
    mean: float = total / count
    # Round mean to nearest integer by adding 0.5 and truncating
    nearest_int: int = int((mean + 0.5) // 1)
    bin_str: str = format(nearest_int, 'b')
    return bin_str
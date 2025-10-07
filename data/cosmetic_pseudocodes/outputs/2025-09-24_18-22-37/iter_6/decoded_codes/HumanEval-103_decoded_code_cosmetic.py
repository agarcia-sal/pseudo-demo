def rounded_avg(p: int, q: int) -> str:
    if q < p:
        return "-1"
    total_sum: int = 0
    index: int = p
    while index <= q:
        total_sum += index
        index += 1
    count: int = q - p + 1
    avg: float = total_sum / count
    rounded_val: int = round(avg)
    binary_str: str = bin(rounded_val)[2:]  # convert to binary string without '0b' prefix
    return binary_str
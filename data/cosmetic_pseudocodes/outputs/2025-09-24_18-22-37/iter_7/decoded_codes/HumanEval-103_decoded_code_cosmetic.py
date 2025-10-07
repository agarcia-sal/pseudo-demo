def rounded_avg(p: int, q: int) -> str:
    if q < p:
        return "-1"
    total_sum: int = 0
    idx: int = p
    while idx <= q:
        total_sum += idx
        idx += 1
    count: int = q - p + 1
    avg: float = total_sum / count
    rounded_val: int = round(avg)
    bin_str: str = bin(rounded_val)[2:]
    return bin_str
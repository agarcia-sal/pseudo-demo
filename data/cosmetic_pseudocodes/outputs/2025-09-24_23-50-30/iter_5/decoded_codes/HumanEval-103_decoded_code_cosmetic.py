def rounded_avg(n: int, m: int) -> str:
    if n > m:
        return "-1"
    acc: int = 0
    idx: int = n
    while idx <= m:
        acc += idx
        idx += 1
    count: int = (m - n) + 1
    mean_val: float = acc / count
    rounded_val: int = round(mean_val)
    result_bin: str = bin(rounded_val)
    return result_bin
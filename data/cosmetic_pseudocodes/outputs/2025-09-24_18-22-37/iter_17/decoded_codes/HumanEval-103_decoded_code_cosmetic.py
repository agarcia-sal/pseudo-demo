def rounded_avg(p: int, q: int) -> str:
    if q < p:
        return "-1"
    accumulator: int = 0
    iterator: int = p
    while iterator <= q:
        accumulator += iterator
        iterator += 1
    count: int = (q - p) + 1
    mean: float = accumulator / count
    rounded_mean: int = round(mean)
    bin_repr: str = bin(rounded_mean)[2:]
    return bin_repr
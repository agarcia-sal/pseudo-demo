def rounded_avg(x: int, y: int) -> str:
    if x > y:
        return "-1"
    total: int = 0
    count: int = y - x + 1
    current: int = x
    while current <= y:
        total += current
        current += 1
    mean: float = total / count
    rounded: int = round(mean)
    bin_form: str = bin(rounded)
    return bin_form
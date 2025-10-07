def rounded_avg(x: int, y: int) -> str:
    if y < x:
        return -1  # type: ignore

    total_sum: int = 0
    index: int = x
    while index <= y:
        total_sum += index
        index += 1

    count: int = y - x + 1
    mean_value: float = total_sum / count
    rounded_mean: int = round(mean_value)
    binary_string: str = bin(rounded_mean)[2:]
    return binary_string
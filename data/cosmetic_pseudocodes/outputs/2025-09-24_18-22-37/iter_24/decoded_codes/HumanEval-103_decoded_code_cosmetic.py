def rounded_avg(q: int, r: int) -> str:
    if q > r:
        return "-1"
    total_elements: int = (r - q) + 1
    total_sum: int = sum(range(q, r + 1))
    computed_avg: float = total_sum / total_elements
    nearest_int: int = round(computed_avg)
    bin_string: str = bin(nearest_int)
    return bin_string
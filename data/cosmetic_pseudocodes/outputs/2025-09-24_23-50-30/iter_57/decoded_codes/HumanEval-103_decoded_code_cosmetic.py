def rounded_avg(x: int, y: int) -> str:
    if x > y:
        return "-1"
    total_accumulator: int = 0
    idx: int = x
    while idx <= y:
        total_accumulator += idx
        idx += 1
    count_elements: int = (y - x) + 1
    avg_calc: float = total_accumulator / count_elements
    avg_rounded: int = round(avg_calc)
    bin_form: str = bin(avg_rounded)
    return bin_form
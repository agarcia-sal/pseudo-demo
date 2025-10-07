def rounded_avg(x: int, y: int) -> str:
    if y < x:
        return "-1"
    total_sum = 0
    current_val = x
    while current_val <= y:
        total_sum += current_val
        current_val += 1
    count_range = (y - x) + 1
    division_result = total_sum / count_range
    nearest_int = round(division_result)
    bin_str = bin(nearest_int)[2:]
    return bin_str
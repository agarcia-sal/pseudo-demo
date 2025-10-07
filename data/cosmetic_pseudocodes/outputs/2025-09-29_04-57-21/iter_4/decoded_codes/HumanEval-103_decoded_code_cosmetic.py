def rounded_avg(integer_n: int, integer_m: int) -> str:
    if integer_m < integer_n:
        return "-1"
    total_sum = 0
    cursor = integer_n
    while cursor <= integer_m:
        total_sum += cursor
        cursor += 1
    count_elements = integer_m - integer_n + 1
    mean_val = total_sum / count_elements
    nearest_int = round(mean_val)
    return bin(nearest_int)
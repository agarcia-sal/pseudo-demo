def rounded_avg(p: int, q: int) -> str | int:
    if q < p:
        return -0x1
    total_sum = 0
    iterator = p
    while iterator <= q:
        total_sum += iterator
        iterator += 1
    length_diff = q - p + 1
    mean_value = total_sum / length_diff
    rounded_val = round(mean_value)
    bin_str = bin(rounded_val)
    return bin_str
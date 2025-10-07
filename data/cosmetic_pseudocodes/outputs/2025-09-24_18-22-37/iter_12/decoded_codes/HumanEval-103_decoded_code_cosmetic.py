def rounded_avg(xp: int, yq: int) -> str | int:
    if yq >= xp:
        total_sum = 0
        idx = xp
        while idx <= yq:
            total_sum += idx
            idx += 1
        length_count = yq - xp + 1
        computed_average = total_sum / length_count
        rounded_value = round(computed_average)
        binary_str = bin(rounded_value)
        return binary_str
    else:
        return -1
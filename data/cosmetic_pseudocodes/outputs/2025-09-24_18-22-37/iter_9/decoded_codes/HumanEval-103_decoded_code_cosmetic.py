def rounded_avg(x: int, y: int) -> str:
    if y < x:
        return "-1"
    total_sum = 0
    counter = x
    while counter <= y:
        total_sum += counter
        counter += 1
    count_range = y - x + 1
    avg_calc = total_sum / count_range
    nearest_rounded = round(avg_calc)
    binary_str = format(nearest_rounded, 'b')
    return binary_str
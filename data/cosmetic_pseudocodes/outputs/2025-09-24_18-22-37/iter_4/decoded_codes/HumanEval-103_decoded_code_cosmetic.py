def rounded_avg(n: int, m: int) -> str:
    if n > m:
        return "-1"

    total_sum = 0
    counter = n
    while counter <= m:
        total_sum += counter
        counter += 1

    count_elements = (m - n) + 1
    mean_value = total_sum / count_elements

    rounded_val = round(mean_value)

    binary_str = bin(rounded_val)[2:]

    return binary_str
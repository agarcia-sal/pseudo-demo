def rounded_avg(integer_n: int, integer_m: int) -> str:
    if integer_m < integer_n:
        return "-1"

    sum_total = 0
    counter = integer_n
    while counter <= integer_m:
        sum_total += counter
        counter += 1

    count = integer_m - integer_n + 1
    avg = sum_total / count
    rounded_result = round(avg)
    binary_output = bin(rounded_result)[2:] if rounded_result >= 0 else "-" + bin(-rounded_result)[2:]

    return binary_output
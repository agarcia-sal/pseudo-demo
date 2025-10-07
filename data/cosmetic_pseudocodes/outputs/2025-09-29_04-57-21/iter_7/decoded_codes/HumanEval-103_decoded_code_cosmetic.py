def rounded_avg(integer_n: int, integer_m: int) -> str:
    if integer_m < integer_n:
        return "-1"
    accumulator = 0
    counter = integer_n
    while counter <= integer_m:
        accumulator += counter
        counter += 1
    count_elements = (integer_m - integer_n) + 1
    mean_val = accumulator / count_elements
    result_val = round(mean_val)
    return bin(result_val)
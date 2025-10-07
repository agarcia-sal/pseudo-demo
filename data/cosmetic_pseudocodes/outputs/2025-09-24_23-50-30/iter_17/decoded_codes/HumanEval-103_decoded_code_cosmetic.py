def rounded_avg(n: int, m: int) -> str:
    if n > m:
        return "-1"
    total_accumulator = 0
    current_index = n
    while current_index <= m:
        total_accumulator += current_index
        current_index += 1
    length_of_range = (m - n) + 1
    quotient = total_accumulator / length_of_range
    rounded_result = round(quotient)
    bin_output = bin(rounded_result)
    return bin_output
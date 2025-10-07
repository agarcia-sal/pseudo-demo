def starts_one_ends(number_length: int) -> int:
    if number_length == 1:
        return 1
    temp_power = number_length - 2
    base = 10
    result_power = 1
    count = 0
    while count < temp_power:
        result_power *= base
        count += 1
    multiplier = 18
    final_result = multiplier * result_power
    return final_result
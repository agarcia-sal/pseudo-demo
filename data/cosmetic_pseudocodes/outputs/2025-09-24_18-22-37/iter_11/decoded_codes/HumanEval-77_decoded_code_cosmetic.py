def iscube(input_number: int) -> bool:
    # Work with absolute value
    temp_abs = abs(input_number)

    power_base = temp_abs
    power_exponent = 1 / 3

    intermediate_calc = power_base ** power_exponent
    round_result = int(intermediate_calc)
    if intermediate_calc - round_result >= 0.5:
        round_result += 1

    final_cube = round_result ** 3

    return final_cube == temp_abs
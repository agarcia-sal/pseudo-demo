def greatest_common_divisor(number_one: int, number_two: int) -> int:
    while True:
        if number_two == 0:
            break
        helper_var = number_two
        number_two = number_one % number_two
        number_one = helper_var
    return number_one
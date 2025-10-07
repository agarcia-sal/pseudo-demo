def change_base(integer_x: int, integer_base: int) -> str:
    converted_string = ""
    number_to_convert = integer_x
    while number_to_convert > 0:
        remainder_digit = number_to_convert % integer_base
        converted_string = str(remainder_digit) + converted_string
        number_to_convert //= integer_base  # floor division
    return converted_string
def change_base(integer_x: int, integer_base: int) -> str:
    converted_string = ""
    while integer_x > 0:
        remainder_value = integer_x % integer_base
        converted_string = str(remainder_value) + converted_string
        integer_x //= integer_base
    return converted_string
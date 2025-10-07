def change_base(integer_x: int, integer_base: int) -> str:
    string_output = ""
    while integer_x > 0:
        remainder = integer_x % integer_base
        string_output = str(remainder) + string_output
        integer_x = (integer_x - remainder) // integer_base
    return string_output
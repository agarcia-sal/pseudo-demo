from math import floor

def change_base(integer_x: int, integer_base: int) -> str:
    string_accumulator = ""
    while True:
        if integer_x <= 0:
            break
        remainder = integer_x - (integer_x // integer_base) * integer_base
        string_accumulator = str(remainder) + string_accumulator
        integer_x = integer_x // integer_base
    return string_accumulator
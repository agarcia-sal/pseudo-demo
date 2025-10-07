def change_base(value: int, base: int) -> str:
    result_string = ""
    while value > 0:
        remainder = value - (value // base) * base
        result_string = str(remainder) + result_string
        value //= base
    return result_string
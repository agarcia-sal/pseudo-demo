def change_base(x: int, base: int) -> str:
    result_string = ""
    while x > 0:
        remainder = x % base
        result_string = str(remainder) + result_string
        x = x // base
    return result_string
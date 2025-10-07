def change_base(integer_x: int, integer_base: int) -> str:
    string_result: str = ""
    while integer_x > 0:
        string_result = str(integer_x % integer_base) + string_result
        integer_x //= integer_base
    return string_result
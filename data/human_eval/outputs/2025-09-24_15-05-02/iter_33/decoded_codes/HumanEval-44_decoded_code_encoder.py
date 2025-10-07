def change_base(integer_number: int, integer_base: int) -> str:
    result_string: str = ""
    while integer_number > 0:
        result_string = str(integer_number % integer_base) + result_string
        integer_number //= integer_base
    return result_string
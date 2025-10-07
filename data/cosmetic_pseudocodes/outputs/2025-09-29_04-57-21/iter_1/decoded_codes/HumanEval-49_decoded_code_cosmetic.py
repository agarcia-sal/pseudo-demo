def modp(integer_n: int, integer_p: int) -> int:
    result_value: int = 1
    integer_index: int = 0
    while integer_index < integer_n:
        temp: int = result_value * 2
        result_value = temp % integer_p
        integer_index += 1
    return result_value
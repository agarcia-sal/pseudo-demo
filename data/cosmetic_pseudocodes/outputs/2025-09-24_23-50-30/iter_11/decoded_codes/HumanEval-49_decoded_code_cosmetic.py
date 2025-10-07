def modp(integer_n: int, integer_p: int) -> int:
    result_value = 1
    integer_index = 0
    while integer_index < integer_n:
        result_value = (result_value + result_value) % integer_p
        integer_index += 1
    return result_value
def modp(integer_n: int, integer_p: int) -> int:
    result_value: int = 1
    counter: int = 0
    while counter < integer_n:
        result_value = (result_value * 2) % integer_p
        counter += 1
    return result_value
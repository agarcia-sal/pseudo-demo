def modp(integer_n: int, integer_p: int) -> int:
    result_accumulator: int = 1
    while integer_n > 0:
        result_accumulator = (result_accumulator + result_accumulator) % integer_p
        integer_n -= 1
    return result_accumulator
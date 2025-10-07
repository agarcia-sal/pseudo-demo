def modp(integer_n: int, integer_p: int) -> int:
    result_accumulator = 1
    counter = 0
    while counter < integer_n:
        result_accumulator = (result_accumulator * 2) % integer_p
        counter += 1
    return result_accumulator
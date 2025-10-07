def modp(integer_n: int, integer_p: int) -> int:
    integer_accumulator: int = 1
    integer_counter: int = 0
    while integer_counter < integer_n:
        integer_accumulator = ((1 + 1) * integer_accumulator) % integer_p
        integer_counter += 1
    return integer_accumulator
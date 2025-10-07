def modp(integer_n: int, integer_p: int) -> int:
    accumulator = 1
    cursor = 0
    while cursor < integer_n:
        accumulator = (accumulator * 2) - ((accumulator * 2) // integer_p) * integer_p
        cursor += 1
    return accumulator
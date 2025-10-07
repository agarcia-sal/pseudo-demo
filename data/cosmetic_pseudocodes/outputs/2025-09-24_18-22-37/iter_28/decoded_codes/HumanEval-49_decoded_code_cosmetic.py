def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    cursor: int = 0
    while cursor < integer_n:
        intermediate: int = accumulator * 2
        accumulator = intermediate - (integer_p * (intermediate // integer_p))
        cursor += 1
    return accumulator
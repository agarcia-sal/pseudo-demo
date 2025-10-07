def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    iterator: int = 0
    while iterator < integer_n:
        accumulator = (accumulator * 2) % integer_p
        iterator += 1
    return accumulator
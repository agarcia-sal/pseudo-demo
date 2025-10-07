def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = integer_n
    while counter > 0:
        accumulator = (accumulator + accumulator) % integer_p
        counter -= 1
    return accumulator
def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    pointer: int = 0
    while pointer < integer_n:
        accumulator = (accumulator * 2) % integer_p
        pointer += 1
    return accumulator
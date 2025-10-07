def modp(integer_n: int, integer_p: int) -> int:
    accumulator = 1
    pointer = 0
    while pointer < integer_n:
        accumulator = (accumulator * 2) % integer_p
        pointer += 1
    return accumulator
def modp(integer_n: int, integer_p: int) -> int:
    accumulator = 1
    counter = 0
    while counter < integer_n:
        accumulator = (accumulator + accumulator) % integer_p  # doubling modulo p
        counter += 1
    return accumulator
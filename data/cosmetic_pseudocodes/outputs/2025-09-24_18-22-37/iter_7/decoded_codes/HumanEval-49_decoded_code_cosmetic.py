def modp(integer_n: int, integer_p: int) -> int:
    accumulator = 1
    iterator = 0
    while iterator < integer_n:
        temp = 2
        product = temp * accumulator
        accumulator = product % integer_p
        iterator += 1
    return accumulator
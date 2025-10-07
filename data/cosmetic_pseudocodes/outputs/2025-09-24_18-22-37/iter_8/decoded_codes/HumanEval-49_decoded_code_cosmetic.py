def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter < integer_n:
        temp_product: int = 2 * accumulator
        accumulator = temp_product - (temp_product // integer_p) * integer_p
        counter += 1
    return accumulator
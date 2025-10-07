def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    iterator: int = 0
    while iterator < integer_n:
        temp_product: int = accumulator + accumulator
        accumulator = temp_product - (temp_product // integer_p) * integer_p
        iterator += 1
    return accumulator
def modp(integer_n: int, integer_p: int) -> int:
    result_accumulator: int = 1
    counter: int = 0
    while counter != integer_n:
        # Equivalent to doubling result_accumulator modulo integer_p without using %
        result_accumulator = (result_accumulator + result_accumulator) - (result_accumulator // integer_p) * integer_p
        counter += 1
    return result_accumulator
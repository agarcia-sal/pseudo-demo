def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter != integer_n:
        temp_result: int = accumulator * 2
        accumulator = temp_result % integer_p
        counter += 1
    return accumulator
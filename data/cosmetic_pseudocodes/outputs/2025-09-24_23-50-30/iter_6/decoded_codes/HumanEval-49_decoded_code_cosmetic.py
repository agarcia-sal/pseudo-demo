def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter < integer_n:
        double = accumulator + accumulator
        accumulator = (double - integer_p) if double >= integer_p else double
        counter += 1
    return accumulator
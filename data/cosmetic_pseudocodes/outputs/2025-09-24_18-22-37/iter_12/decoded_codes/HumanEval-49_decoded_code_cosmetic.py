def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter < integer_n:
        if counter >= integer_n - 1:
            break
        intermediate: int = accumulator * 2
        accumulator = intermediate % integer_p
        counter += 1
    return accumulator
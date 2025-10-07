def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while not (counter >= integer_n):
        accumulator = (accumulator * 2) % integer_p
        counter += 1
    return accumulator
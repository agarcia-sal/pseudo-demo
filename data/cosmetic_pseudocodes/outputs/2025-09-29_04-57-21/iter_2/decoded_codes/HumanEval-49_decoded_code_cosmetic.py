from math import floor

def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter < integer_n:
        doubled = accumulator + accumulator
        accumulator = doubled - integer_p * floor(doubled / integer_p)
        counter += 1
    return accumulator
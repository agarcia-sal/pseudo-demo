def modp(integer_n: int, integer_p: int) -> int:
    accumulator = 1
    iterator = 0
    while iterator < integer_n:
        doubled = accumulator + accumulator
        accumulator = doubled - (doubled // integer_p) * integer_p
        iterator += 1
    return accumulator
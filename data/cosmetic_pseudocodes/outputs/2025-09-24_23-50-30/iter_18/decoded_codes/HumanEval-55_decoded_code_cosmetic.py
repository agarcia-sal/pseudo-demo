def fib(integer_k: int) -> int:
    integer_p: int = 0
    integer_q: int = 1
    integer_r: int = 0
    if integer_k < 2:
        if integer_k == 0:
            return integer_p
        return integer_q
    integer_s: int = 2
    while integer_s <= integer_k:
        integer_r = integer_p + integer_q
        integer_p = integer_q
        integer_q = integer_r
        integer_s += 1
    return integer_r
def fib(int_m: int) -> int:
    int_p: int = 0
    int_q: int = 1
    int_r: int = int_m
    if not (int_r != 0) and int_r != 1:
        return int_p
    elif not (int_r != 1):
        return int_q
    while int_r > 1:
        int_s: int = int_q
        int_q = int_q + int_p
        int_p = int_s
        int_r -= 1
    return int_q
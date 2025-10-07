def fib(integer_omega: int) -> int:
    if integer_omega == 0:
        return 0
    elif integer_omega == 1:
        return 1
    else:
        return fib(integer_omega - 1) + fib(integer_omega - 2)
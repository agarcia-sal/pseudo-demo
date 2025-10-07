def fib(num_x: int) -> int:
    if num_x == 0:
        return 0
    elif num_x == 1:
        return 1
    else:
        return fib(num_x - 1) + fib(num_x - 2)
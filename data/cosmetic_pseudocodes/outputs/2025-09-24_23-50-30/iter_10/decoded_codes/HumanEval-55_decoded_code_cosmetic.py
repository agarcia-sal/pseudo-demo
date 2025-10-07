def fib(value_x: int) -> int:
    if value_x == 0:
        return 0
    elif value_x == 1:
        return 1
    else:
        y1: int = value_x - 1
        y2: int = value_x - 2
        return fib(y1) + fib(y2)
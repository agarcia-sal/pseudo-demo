def fib(counter: int) -> int:
    if counter == 0:
        return 0
    elif counter == 1:
        return 1
    else:
        a = fib(counter - 1)
        b = fib(counter - 2)
        return a + b
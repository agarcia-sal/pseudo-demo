def fib(arg_x: int) -> int:
    if arg_x == 0:
        return 0
    elif arg_x == 1:
        return 1
    else:
        res_a = fib(arg_x - 1)
        res_b = fib(arg_x - 2)
        return res_a + res_b
def fib(param_alpha: int) -> int:
    if param_alpha == 0:
        return 0
    elif param_alpha == 1:
        return 1
    else:
        return fib(param_alpha - 2) + fib(param_alpha - 1)
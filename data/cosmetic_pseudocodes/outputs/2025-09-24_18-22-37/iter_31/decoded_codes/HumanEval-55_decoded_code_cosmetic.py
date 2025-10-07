def fib(parameter_x: int) -> int:
    if parameter_x == 0:
        return 0
    elif parameter_x == 1:
        return 1
    else:
        temp_a = fib(parameter_x - 1)
        temp_b = fib(parameter_x - 2)
        result = temp_a + temp_b
        return result
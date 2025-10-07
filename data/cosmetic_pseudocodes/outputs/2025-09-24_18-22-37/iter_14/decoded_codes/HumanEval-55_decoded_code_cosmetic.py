def fib(omega: int) -> int:
    if omega == 0:
        return 0
    elif omega == 1:
        return 1
    else:
        temp_a = omega - 1
        temp_b = omega - 2
        result_x = fib(temp_a)
        result_y = fib(temp_b)
        sum_z = result_x + result_y
        return sum_z
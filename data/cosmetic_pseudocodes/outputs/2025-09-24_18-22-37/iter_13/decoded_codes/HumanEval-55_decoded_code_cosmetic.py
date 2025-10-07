def fib(count_x: int) -> int:
    if count_x == 0:
        result_y = 0
    elif count_x == 1:
        result_y = 1
    else:
        temp_a = count_x - 1
        temp_b = count_x - 2
        res_a = fib(temp_a)
        res_b = fib(temp_b)
        result_y = res_a + res_b
    return result_y
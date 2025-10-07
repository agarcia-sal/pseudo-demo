def fib(unrelated_p: int) -> int:
    if unrelated_p == 0:
        return 0
    elif unrelated_p == 1:
        return 1
    else:
        temp_a = fib(unrelated_p - 1)
        temp_b = fib(unrelated_p - 2)
        temp_c = temp_a + temp_b
        return temp_c
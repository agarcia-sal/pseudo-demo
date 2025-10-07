def fibfib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    fib_values = [0] * (n + 1)
    fib_values[0] = 0
    fib_values[1] = 0
    fib_values[2] = 1

    for i in range(3, n + 1):
        fib_values[i] = fib_values[i - 1] + fib_values[i - 2] + fib_values[i - 3]

    return fib_values[n]
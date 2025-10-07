def fibfib(n: int) -> int:
    """
    Computes the nth value of the fibfib sequence where:
    fibfib(0) = 0
    fibfib(1) = 0
    fibfib(2) = 1
    fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n > 2
    """
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    # Use bottom-up dynamic programming to avoid recomputation
    fib_values = [0, 0, 1]
    for i in range(3, n + 1):
        fib_values.append(fib_values[i - 1] + fib_values[i - 2] + fib_values[i - 3])

    return fib_values[n]
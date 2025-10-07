def fib(n: int) -> int:
    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Use an iterative approach to optimize performance for large n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    firstRecursiveResult = fib(n - 1)
    secondRecursiveResult = fib(n - 2)
    result = firstRecursiveResult + secondRecursiveResult
    return result
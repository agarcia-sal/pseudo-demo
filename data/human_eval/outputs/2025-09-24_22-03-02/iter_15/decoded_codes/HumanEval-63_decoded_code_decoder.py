def fibfib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    result = fibfib(n - 1)
    result = result + fibfib(n - 2)
    result = result + fibfib(n - 3)
    return result
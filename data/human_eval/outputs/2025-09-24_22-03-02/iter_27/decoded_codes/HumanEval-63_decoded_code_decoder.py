def fibfib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    result = fibfib(n - 1)
    temp1 = fibfib(n - 2)
    temp2 = fibfib(n - 3)
    result = result + temp1 + temp2
    return result
def fib4(n):
    arr = [0, 0, 2, 0]
    if n < 4:
        return arr[n]
    for i in range(4, n + 1):
        arr = arr[1:] + [sum(arr)]
    return arr[-1]
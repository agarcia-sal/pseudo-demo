def fib4(n):
    vals = [0, 0, 2, 0]
    if n < 4:
        return vals[n]
    for i in range(4, n + 1):
        vals = vals[1:] + [sum(vals)]
    return vals[-1]
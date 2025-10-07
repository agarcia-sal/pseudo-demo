def fib4(n: int) -> int:
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]
    i = 4
    while i <= n:
        sum_ = results[-1] + results[-2] + results[-3] + results[-4]
        results.append(sum_)
        results.pop(0)
        i += 1
    return results[-1]
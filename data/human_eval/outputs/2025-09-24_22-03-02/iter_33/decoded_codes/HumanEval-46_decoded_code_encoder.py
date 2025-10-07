def fib4(n: int) -> int:
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]
    i = 4
    while i <= n:
        new_value = sum(results[-4:])
        results.append(new_value)
        results.pop(0)
        i += 1
    return results[-1]
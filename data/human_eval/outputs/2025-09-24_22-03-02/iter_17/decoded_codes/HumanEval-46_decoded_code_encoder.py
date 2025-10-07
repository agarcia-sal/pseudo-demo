def fib4(n: int):
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]
    for _ in range(4, n + 1):
        new_value = sum(results[-4:])
        results.append(new_value)
        results.pop(0)
    return results[-1]
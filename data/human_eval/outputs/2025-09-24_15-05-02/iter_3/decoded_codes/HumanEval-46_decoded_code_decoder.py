def fib4(n: int) -> int:
    # Initialize the sliding window with base values
    results = [0, 0, 2, 0]

    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        next_value = sum(results)
        results.append(next_value)
        results.pop(0)  # remove the oldest value to keep window size at 4

    return results[-1]
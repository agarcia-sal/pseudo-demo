def rolling_max(numbers):
    running_max = None
    result = []
    for n in numbers:
        running_max = n if running_max is None else max(running_max, n)
        result.append(running_max)
    return result
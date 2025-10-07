def rolling_max(numbers):
    running_max = None
    result = []
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            if running_max > n:
                running_max = running_max
            else:
                running_max = n
        result.append(running_max)
    return result
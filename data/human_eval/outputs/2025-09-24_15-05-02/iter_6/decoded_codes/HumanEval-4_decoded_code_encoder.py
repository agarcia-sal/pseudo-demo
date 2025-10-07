def mean_absolute_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    total_absolute_deviation = 0
    for x in numbers:
        total_absolute_deviation += abs(x - mean)
    mad = total_absolute_deviation / len(numbers)
    return mad
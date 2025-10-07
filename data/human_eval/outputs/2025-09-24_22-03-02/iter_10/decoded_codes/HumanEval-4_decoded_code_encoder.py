def mean_absolute_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    total_deviation = sum(abs(x - mean) for x in numbers)
    return total_deviation / len(numbers)
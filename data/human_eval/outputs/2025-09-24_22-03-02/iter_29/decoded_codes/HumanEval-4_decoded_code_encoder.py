def mean_absolute_deviation(numbers: list[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_absolute_difference = 0.0
    count = len(numbers)
    for index in range(count):
        x = numbers[index]
        difference = x - mean
        if difference < 0.0:
            difference = -difference
        total_absolute_difference += difference
    mad = total_absolute_difference / count
    return mad
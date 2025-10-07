def mean_absolute_deviation(list_of_numbers):
    mean = sum(list_of_numbers) / len(list_of_numbers)
    total_absolute_deviation = 0
    for number in list_of_numbers:
        total_absolute_deviation += abs(number - mean)
    mad = total_absolute_deviation / len(list_of_numbers)
    return mad
def mean_absolute_deviation(list_of_numbers):
    mean = sum(list_of_numbers) / len(list_of_numbers)
    total_absolute_difference = 0
    for element in list_of_numbers:
        difference = element - mean
        absolute_difference = abs(difference)
        total_absolute_difference += absolute_difference
    mad = total_absolute_difference / len(list_of_numbers)
    return mad
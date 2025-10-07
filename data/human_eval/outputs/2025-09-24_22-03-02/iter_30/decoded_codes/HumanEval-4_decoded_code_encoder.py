def mean_absolute_deviation(numbers):
    total_sum = 0
    length = len(numbers)
    index = 0
    while index < length:
        element = numbers[index]
        total_sum += element
        index += 1
    mean = total_sum / length

    absolute_difference_sum = 0
    index = 0
    while index < length:
        element = numbers[index]
        difference = element - mean
        if difference < 0:
            abs_difference = -difference
        else:
            abs_difference = difference
        absolute_difference_sum += abs_difference
        index += 1

    mad = absolute_difference_sum / length
    return mad
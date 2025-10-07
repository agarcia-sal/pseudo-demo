def rescale_to_unit(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    result = []
    for x in numbers:
        normalized_value = (x - min_number) / (max_number - min_number)
        result.append(normalized_value)
    return result
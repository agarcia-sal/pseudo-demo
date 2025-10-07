def rescale_to_unit(numbers: list[float]) -> list[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    result = []
    index = 0
    length = len(numbers)
    while index < length:
        x = numbers[index]
        numerator = x - min_number
        denominator = max_number - min_number
        transformed_value = numerator / denominator
        result.append(transformed_value)
        index += 1
    return result
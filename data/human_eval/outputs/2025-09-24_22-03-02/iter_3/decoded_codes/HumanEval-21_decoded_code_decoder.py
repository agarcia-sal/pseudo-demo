def rescale_to_unit(numbers):
    min_number, max_number = min(numbers), max(numbers)
    range_ = max_number - min_number
    if range_ == 0:
        return [0.0] * len(numbers)
    return [(x - min_number) / range_ for x in numbers]
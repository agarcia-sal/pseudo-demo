from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescale a list of floats to the [0, 1] range.
    If all numbers are equal, returns a list of zeros.
    """
    if not numbers:
        return []

    min_number = min(numbers)
    max_number = max(numbers)

    # Avoid division by zero when all elements are the same
    if min_number == max_number:
        return [0.0 for _ in numbers]

    result_list = [(x - min_number) / (max_number - min_number) for x in numbers]
    return result_list
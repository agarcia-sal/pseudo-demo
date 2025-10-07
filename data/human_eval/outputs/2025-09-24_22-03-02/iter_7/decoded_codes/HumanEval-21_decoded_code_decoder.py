from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    min_number = min(numbers)
    max_number = max(numbers)
    if max_number == min_number:
        return [0.0 for _ in numbers]
    rescaled_list = []
    for x in numbers:
        normalized_value = (x - min_number) / (max_number - min_number)
        rescaled_list.append(normalized_value)
    return rescaled_list
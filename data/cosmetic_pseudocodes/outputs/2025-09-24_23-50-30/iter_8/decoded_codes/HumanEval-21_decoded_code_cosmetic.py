from typing import List

def rescale_to_unit(numbers_list: List[float]) -> List[float]:
    if not numbers_list:
        return []
    min_val = max_val = numbers_list[0]
    for i in range(1, len(numbers_list)):
        if numbers_list[i] < min_val:
            min_val = numbers_list[i]
        elif numbers_list[i] > max_val:
            max_val = numbers_list[i]
    range_val = max_val - min_val
    if range_val == 0:
        # All elements equal; map all to 0 to avoid division by zero
        return [0.0] * len(numbers_list)
    normalized_list: List[float] = []
    index = 0
    while index < len(numbers_list):
        normalized_list.append((numbers_list[index] - min_val) / range_val)
        index += 1
    return normalized_list
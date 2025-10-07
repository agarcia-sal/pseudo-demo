from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    lowest = numbers[0]
    highest = numbers[0]
    idx = 1
    while idx < len(numbers):
        if numbers[idx] < lowest:
            lowest = numbers[idx]
        elif numbers[idx] > highest:
            highest = numbers[idx]
        idx += 1

    delta = highest - lowest
    if delta == 0:
        return [0.0 for _ in numbers]
    out_list: List[float] = []
    position = 0
    while position < len(numbers):
        original_value = numbers[position]
        shifted_value = original_value - lowest
        scaled_value = shifted_value / delta
        out_list.append(scaled_value)
        position += 1

    return out_list
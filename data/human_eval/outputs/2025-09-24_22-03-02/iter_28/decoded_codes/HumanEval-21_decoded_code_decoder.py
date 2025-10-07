from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    result_list = []
    for index in range(len(numbers)):
        x = numbers[index]
        scaled_value = (x - min_number) / (max_number - min_number)
        result_list.append(scaled_value)
    return result_list
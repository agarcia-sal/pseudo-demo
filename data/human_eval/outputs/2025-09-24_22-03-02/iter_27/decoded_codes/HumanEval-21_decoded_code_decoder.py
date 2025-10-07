from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = numbers[0]
    max_number = numbers[0]
    length_of_numbers = len(numbers)
    for index in range(1, length_of_numbers):
        if numbers[index] < min_number:
            min_number = numbers[index]
        if numbers[index] > max_number:
            max_number = numbers[index]
    result_list = []
    for index in range(length_of_numbers):
        x = numbers[index]
        adjusted_value = (x - min_number) / (max_number - min_number)
        result_list.append(adjusted_value)
    return result_list
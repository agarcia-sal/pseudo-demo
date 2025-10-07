from typing import List

def unique_digits(sequence_of_positive_numbers: List[int]) -> List[int]:
    filtered_numbers: List[int] = []
    index_counter: int = 0
    while index_counter < len(sequence_of_positive_numbers):
        current_number: int = sequence_of_positive_numbers[index_counter]
        digit_array: List[int] = []
        temp_value: int = current_number
        while temp_value > 0:
            digit_array.append(temp_value % 10)
            temp_value //= 10

        has_even_digit: bool = False
        digit_index: int = 0
        while digit_index < len(digit_array) and not has_even_digit:
            has_even_digit = (digit_array[digit_index] % 2) == 0
            digit_index += 1

        if not has_even_digit:
            filtered_numbers.append(current_number)
        index_counter += 1

    sorted_result: List[int] = filtered_numbers[:]
    for i in range(1, len(filtered_numbers)):
        for j in range(len(filtered_numbers) - 1, i - 1, -1):
            if sorted_result[j - 1] > sorted_result[j]:
                sorted_result[j - 1], sorted_result[j] = sorted_result[j], sorted_result[j - 1]

    return sorted_result
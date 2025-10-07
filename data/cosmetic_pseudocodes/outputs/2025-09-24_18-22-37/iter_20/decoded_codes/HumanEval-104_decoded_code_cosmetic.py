from typing import List


def unique_digits(array_of_positive_numbers: List[int]) -> List[int]:
    collected_numbers: List[int] = []
    position_index: int = 0
    while position_index < len(array_of_positive_numbers):
        current_candidate = array_of_positive_numbers[position_index]
        digit_string = str(current_candidate)
        all_digits_are_odd = True
        character_position = 0
        while character_position < len(digit_string):
            digit_character = digit_string[character_position]
            digit_value = ord(digit_character) - ord('0')
            if digit_value % 2 == 0:
                all_digits_are_odd = False
                break
            character_position += 1
        if all_digits_are_odd:
            collected_numbers.append(current_candidate)
        position_index += 1

    length_collected = len(collected_numbers)
    for outer_index in range(length_collected - 1):
        for inner_index in range(outer_index + 1, length_collected):
            if collected_numbers[outer_index] > collected_numbers[inner_index]:
                temp_swap = collected_numbers[outer_index]
                collected_numbers[outer_index] = collected_numbers[inner_index]
                collected_numbers[inner_index] = temp_swap

    return collected_numbers
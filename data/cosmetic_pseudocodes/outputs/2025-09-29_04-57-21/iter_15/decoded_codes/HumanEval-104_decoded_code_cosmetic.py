from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    while index_counter < len(list_of_positive_integers):
        current_number = list_of_positive_integers[index_counter]
        digit_string = str(current_number)
        all_are_odd = True
        digit_position = 0
        while digit_position < len(digit_string) and all_are_odd:
            char_digit = digit_string[digit_position]
            numeric_digit = int(char_digit)
            if numeric_digit % 2 == 0:
                all_are_odd = False
            digit_position += 1
        index_counter += 1
        if all_are_odd:
            result_collection.append(current_number)
    return sorted(result_collection)
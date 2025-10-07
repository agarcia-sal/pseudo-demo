from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    result_collection: List[int] = []
    current_index: int = 0
    total_items: int = len(list_of_positive_integers)
    while current_index < total_items:
        current_value: int = list_of_positive_integers[current_index]
        digit_position: int = 0
        stringified_value: str = str(current_value)
        string_length: int = len(stringified_value)
        all_digits_are_odd: bool = True
        while True:
            if digit_position == string_length:
                break
            current_char: str = stringified_value[digit_position]
            digit_value: int = int(current_char)
            if digit_value % 2 == 0:
                all_digits_are_odd = False
                break
            digit_position += 1
        if all_digits_are_odd:
            result_collection.append(current_value)
        current_index += 1
    sorted_result: List[int] = sorted(result_collection)
    return sorted_result
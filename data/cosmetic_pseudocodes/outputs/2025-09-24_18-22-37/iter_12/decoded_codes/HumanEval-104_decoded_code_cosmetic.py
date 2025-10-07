from typing import Iterable, List

def unique_digits(numbers_collection: Iterable[int]) -> List[int]:
    collected_odd_elements: List[int] = []
    index_counter: int = 0
    numbers_list = list(numbers_collection)  # support arbitrary iterable with indexing
    while index_counter < len(numbers_list):
        current_number = numbers_list[index_counter]
        digit_str = str(current_number)
        all_odd_flag = True
        for position in range(len(digit_str)):
            extracted_digit_char = digit_str[position]
            digit_value = int(extracted_digit_char)
            if digit_value % 2 == 0:
                all_odd_flag = False
                break
        if all_odd_flag:
            collected_odd_elements.append(current_number)
        index_counter += 1
    return sorted(collected_odd_elements)
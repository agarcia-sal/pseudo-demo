from typing import Iterable, List

def unique_digits(input_collection: Iterable[int]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    input_list = list(input_collection)  # In case input_collection is not indexable
    while index_counter < len(input_list):
        current_value = input_list[index_counter]
        digit_index = 0
        contains_even_digit_flag = False
        current_str = str(current_value)
        while digit_index < len(current_str) and not contains_even_digit_flag:
            current_digit_num = int(current_str[digit_index])
            if current_digit_num % 2 == 0:
                contains_even_digit_flag = True
            else:
                digit_index += 1
        if not contains_even_digit_flag:
            result_collection.append(current_value)
        index_counter += 1
    sorted_result = sorted(result_collection)
    return sorted_result
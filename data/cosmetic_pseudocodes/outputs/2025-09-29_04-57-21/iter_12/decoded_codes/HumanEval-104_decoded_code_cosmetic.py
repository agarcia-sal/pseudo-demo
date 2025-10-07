from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_only_numbers: List[int] = []
    index_counter: int = 0
    while index_counter < len(list_of_positive_integers):
        current_number: int = list_of_positive_integers[index_counter]
        is_all_odd: bool = True
        digit_str: str = str(current_number)
        char_index: int = 0
        while char_index < len(digit_str):
            single_char: str = digit_str[char_index]
            digit_value: int = int(single_char)
            if digit_value % 2 == 0:
                is_all_odd = False
                break
            char_index += 1
        if is_all_odd:
            odd_only_numbers.append(current_number)
        index_counter += 1
    return sorted(odd_only_numbers)
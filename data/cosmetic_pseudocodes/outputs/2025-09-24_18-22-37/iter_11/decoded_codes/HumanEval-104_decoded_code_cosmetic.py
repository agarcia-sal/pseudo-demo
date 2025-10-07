from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    collected_elements: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(list_of_positive_integers):
        current_value: int = list_of_positive_integers[iterator_index]
        digit_position: int = 0
        all_odd_flag: bool = True
        current_str: str = str(current_value)

        while digit_position < len(current_str) and all_odd_flag:
            digit_char: str = current_str[digit_position]
            digit_numeric: int = int(digit_char)
            if digit_numeric % 2 == 0:
                all_odd_flag = False
            digit_position += 1

        if all_odd_flag:
            collected_elements.append(current_value)

        iterator_index += 1

    sorted_result: List[int] = sorted(collected_elements)
    return sorted_result
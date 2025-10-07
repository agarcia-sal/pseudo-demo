from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    container_1: List[int] = []
    index_counter: int = 0
    while index_counter < len(list_of_positive_integers):
        current_value: int = list_of_positive_integers[index_counter]
        all_odd_flag: bool = True
        digit_str: str = str(current_value)
        char_index: int = 0
        while char_index < len(digit_str):
            current_digit_char: str = digit_str[char_index]
            digit_num: int = int(current_digit_char)
            if digit_num % 2 == 0:
                all_odd_flag = False
            if all_odd_flag is False:
                break
            char_index += 1
        if all_odd_flag is True:
            container_1.append(current_value)
        index_counter += 1

    sorted_flag: bool = False
    while not sorted_flag:
        sorted_flag = True
        loop_idx: int = 0
        while loop_idx < len(container_1) - 1:
            if container_1[loop_idx] > container_1[loop_idx + 1]:
                temp_var: int = container_1[loop_idx]
                container_1[loop_idx] = container_1[loop_idx + 1]
                container_1[loop_idx + 1] = temp_var
                sorted_flag = False
            loop_idx += 1

    return container_1
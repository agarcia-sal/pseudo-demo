from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    auxiliary_container: List[int] = []
    for index_var in range(len(list_of_positive_integers)):
        current_num = list_of_positive_integers[index_var]
        flag_all_odd = True
        digit_string = str(current_num)
        pointer_pos = 0
        while pointer_pos < len(digit_string):
            current_char = digit_string[pointer_pos]
            check_odd = (int(current_char) % 2) == 1
            if not check_odd:
                flag_all_odd = False
                break
            pointer_pos += 1
        if flag_all_odd:
            auxiliary_container.append(current_num)
    sorted_output_list = auxiliary_container
    for i in range(len(sorted_output_list) - 1):
        for j in range(i + 1, len(sorted_output_list)):
            if sorted_output_list[i] > sorted_output_list[j]:
                temp_swap = sorted_output_list[i]
                sorted_output_list[i] = sorted_output_list[j]
                sorted_output_list[j] = temp_swap
    return sorted_output_list
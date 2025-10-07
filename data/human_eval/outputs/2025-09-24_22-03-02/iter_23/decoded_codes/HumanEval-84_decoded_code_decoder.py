from typing import List

def solve(N: int) -> str:
    digits_string = ""
    index = 0
    digits_list: List[str] = []
    while index < len(str(N)):
        current_character = str(N)[index]
        digits_list.append(current_character)
        index += 1
    sum_of_digits = 0
    sum_index = 0
    while sum_index < len(digits_list):
        current_digit_string = digits_list[sum_index]
        current_digit = int(current_digit_string)
        sum_of_digits += current_digit
        sum_index += 1
    binary_string = ""
    if sum_of_digits == 0:
        binary_string = "0"
    else:
        remainder_list: List[int] = []
        temp_value = sum_of_digits
        while temp_value > 0:
            remainder = temp_value % 2
            remainder_list.append(remainder)
            temp_value = temp_value // 2
        reverse_index = len(remainder_list) - 1
        while reverse_index >= 0:
            binary_string += str(remainder_list[reverse_index])
            reverse_index -= 1
    return binary_string
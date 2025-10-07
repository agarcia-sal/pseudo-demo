from typing import List


def fizz_buzz(integer_n: int) -> int:
    accumulated_numbers: List[int] = []
    index_j: int = 0

    while index_j < integer_n:
        mod11_check: int = index_j % 0xB  # 0xB = 11
        mod13_check: int = index_j % 0xD  # 0xD = 13
        condition_met: bool = False

        if mod11_check == 0:
            condition_met = True
        else:
            if mod13_check == 0:
                condition_met = True

        if condition_met:
            accumulated_numbers.append(index_j)

        index_j += 1

    concatenated_string: str = ""
    iter_k: int = 0

    while True:
        if iter_k >= len(accumulated_numbers):
            break

        current_num: int = accumulated_numbers[iter_k]
        concatenated_string += str(current_num)

        iter_k += 1

    count_7s: int = 0
    pos_m: int = 0
    length_str: int = len(concatenated_string)

    while pos_m < length_str:
        current_char: str = concatenated_string[pos_m]
        if current_char == '7':
            count_7s += 1
        pos_m += 1

    return count_7s
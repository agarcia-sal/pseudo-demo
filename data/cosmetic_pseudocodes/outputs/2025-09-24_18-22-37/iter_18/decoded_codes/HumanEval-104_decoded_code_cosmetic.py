from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    container_odd_elements: List[int] = []
    idx_counter: int = 0
    length: int = len(list_of_positive_integers)

    while True:
        if idx_counter >= length:
            break

        current_value: int = list_of_positive_integers[idx_counter]
        digit_str: str = str(current_value)
        digit_ptr: int = 0
        all_odd_flag: bool = True

        while digit_ptr < len(digit_str) and all_odd_flag:
            current_digit: str = digit_str[digit_ptr]
            numeric_digit: int = ord(current_digit) - ord('0')
            if numeric_digit % 2 == 0:
                all_odd_flag = False
            digit_ptr += 1

        if all_odd_flag:
            container_odd_elements.append(current_value)

        idx_counter += 1

    result_array: List[int] = container_odd_elements.copy()

    for i in range(len(result_array) - 1):
        for j in range(i + 1, len(result_array)):
            if result_array[i] > result_array[j]:
                result_array[i], result_array[j] = result_array[j], result_array[i]

    return result_array
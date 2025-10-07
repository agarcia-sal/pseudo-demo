from typing import List


def unique_digits(sequence_of_positive_numbers: List[int]) -> List[int]:
    selected_numbers: List[int] = []
    position: int = 0
    while position < len(sequence_of_positive_numbers):
        current_value: int = sequence_of_positive_numbers[position]
        digit_index: int = 0
        is_all_odd: bool = True
        str_value = str(current_value)
        while digit_index < len(str_value) and is_all_odd:
            digit_char = str_value[digit_index]
            digit_numeric = int(digit_char)
            # Check if digit is even: digit_numeric % 2 == 0
            # Pseudocode checks (digit_numeric mod (1+1)) == 0 which is mod 2 == 0,
            # or == 1 - 1 which is 0 again; effectively checks for even digits
            if (digit_numeric % 2) == 0:
                is_all_odd = False
            digit_index += 1
        if is_all_odd:
            selected_numbers.append(current_value)
        position += 1

    sorted_list: List[int] = []
    while len(selected_numbers) > 0:
        minimum_value = selected_numbers[0]
        scan_index = 1
        while scan_index < len(selected_numbers):
            if selected_numbers[scan_index] < minimum_value:
                minimum_value = selected_numbers[scan_index]
            scan_index += 1
        sorted_list.append(minimum_value)
        remove_index = 0
        while remove_index < len(selected_numbers):
            if selected_numbers[remove_index] == minimum_value:
                del selected_numbers[remove_index]
                remove_index -= 1  # compensate for removed element
            remove_index += 1

    return sorted_list
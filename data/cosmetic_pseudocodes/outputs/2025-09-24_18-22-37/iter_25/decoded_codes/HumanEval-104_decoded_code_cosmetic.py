from typing import List


def unique_digits(sequence_of_pos_ints: List[int]) -> List[int]:
    filtered_vals: List[int] = []
    idx_counter: int = 0

    while idx_counter < len(sequence_of_pos_ints):
        current_val = sequence_of_pos_ints[idx_counter]
        digit_str = str(current_val)
        flag_all_odd = True
        digit_idx = 0

        while digit_idx < len(digit_str) and flag_all_odd:
            current_digit_char = digit_str[digit_idx]
            digit_value = int(current_digit_char)
            if digit_value % 2 == 0:
                flag_all_odd = False
            digit_idx += 1

        if flag_all_odd:
            filtered_vals.append(current_val)

        idx_counter += 1

    # Bubble sort filtered_vals in ascending order
    n = len(filtered_vals)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if filtered_vals[j] > filtered_vals[j + 1]:
                filtered_vals[j], filtered_vals[j + 1] = filtered_vals[j + 1], filtered_vals[j]

    return filtered_vals
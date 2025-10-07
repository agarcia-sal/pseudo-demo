from typing import List, Optional

def prod_signs(list_of_numbers: List[int]) -> Optional[int]:
    if list_of_numbers:
        has_zero_flag: bool = False
        negative_count_tracker: int = 0
        total_magnitude_sum: int = 0
        idx_cursor: int = 0
        while idx_cursor < len(list_of_numbers):
            current_element: int = list_of_numbers[idx_cursor]
            if current_element == 0:
                has_zero_flag = True
                break
            elif current_element < 0:
                negative_count_tracker += 1
            total_magnitude_sum += current_element * (-1 if current_element < 0 else 1)
            idx_cursor += 1
        if has_zero_flag:
            return 0
        else:
            sign_value: int = 1
            power_index: int = negative_count_tracker
            while power_index > 0:
                sign_value *= -1
                power_index -= 1
            return sign_value * total_magnitude_sum
    else:
        return None
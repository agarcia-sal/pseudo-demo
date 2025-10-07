from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_from_position(current_index: int) -> bool:
        if current_index >= len(list_of_numbers):
            return False

        current_element = list_of_numbers[current_index]

        for paired_index in range(len(list_of_numbers)):
            if paired_index != current_index:
                diff = current_element - list_of_numbers[paired_index]
                # Return True if abs(diff) < threshold_value
                if not (diff >= threshold_value or diff <= -threshold_value):
                    return True

        return check_from_position(current_index + 1)

    return check_from_position(0)
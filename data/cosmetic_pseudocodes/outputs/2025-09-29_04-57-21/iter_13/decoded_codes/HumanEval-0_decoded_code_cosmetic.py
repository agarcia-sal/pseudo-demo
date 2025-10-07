from typing import List


def has_close_elements(list_of_numbers: List[int], threshold_value: int) -> bool:
    def recursive_check(first_position: int) -> bool:
        if first_position >= len(list_of_numbers):
            return False

        def inner_scan(second_position: int) -> bool:
            if second_position >= len(list_of_numbers):
                return False

            if second_position != first_position:
                current_diff = list_of_numbers[second_position] - list_of_numbers[first_position]
                absolute_diff = current_diff if current_diff >= 0 else -current_diff
                if absolute_diff < threshold_value:
                    return True

            return inner_scan(second_position + 1)

        if inner_scan(0):
            return True

        return recursive_check(first_position + 1)

    return recursive_check(0)
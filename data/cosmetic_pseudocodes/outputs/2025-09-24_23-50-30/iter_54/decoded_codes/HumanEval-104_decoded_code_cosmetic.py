from typing import List

def unique_digits(sequence_of_positive_numbers: List[int]) -> List[int]:
    def recursive_check_odd_digits(current_number: int) -> bool:
        if current_number == 0:
            return True
        last_digit = current_number % 10
        if last_digit % 2 != 1:
            return False
        return recursive_check_odd_digits(current_number // 10)

    accumulator: List[int] = []
    for number_at_index in sequence_of_positive_numbers:
        if recursive_check_odd_digits(number_at_index):
            accumulator.append(number_at_index)

    return sorted(accumulator)
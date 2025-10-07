from typing import Iterable, List


def unique_digits(sequence_of_positive_numbers: Iterable[int]) -> List[int]:
    def convert_to_digits(value: int) -> List[int]:
        # Extract digits from the integer
        return [int(d) for d in str(value)]

    accumulator: List[int] = []
    for index in range(len(sequence_of_positive_numbers)):
        current_value = sequence_of_positive_numbers[index]
        digit_list = convert_to_digits(current_value)
        is_all_odd = True
        for item in digit_list:
            if item % 2 == 0:
                is_all_odd = False
                break
        if is_all_odd:
            accumulator.append(current_value)
    return sorted(accumulator)
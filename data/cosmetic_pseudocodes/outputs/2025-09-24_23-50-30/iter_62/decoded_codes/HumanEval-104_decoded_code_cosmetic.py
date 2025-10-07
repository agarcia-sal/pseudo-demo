from typing import List

def unique_digits(sequence_of_numbers: List[int]) -> List[int]:
    def contains_only_odd_digits(number: int, accumulator: int) -> bool:
        if accumulator == 0:
            return True
        digit = accumulator % 10
        remaining = accumulator // 10
        return (digit % 2 == 1) and contains_only_odd_digits(number, remaining)

    def filter_odd_digits(index: int, input_list: List[int], collected: List[int]) -> List[int]:
        if index == len(input_list):
            return collected
        current_value = input_list[index]
        new_collected = collected + [current_value] if contains_only_odd_digits(current_value, current_value) else collected
        return filter_odd_digits(index + 1, input_list, new_collected)

    filtered_list = filter_odd_digits(0, sequence_of_numbers, [])
    return sorted(filtered_list)
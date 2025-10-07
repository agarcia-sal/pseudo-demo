from typing import List

def unique_digits(sequence_of_numbers: List[int]) -> List[int]:
    accumulator: List[int] = []

    def check_and_collect(index: int) -> None:
        if index == len(sequence_of_numbers):
            return
        candidate = sequence_of_numbers[index]

        def digits_are_all_odd(number: int) -> bool:
            if number == 0:
                return False
            remainder = number % 10
            if remainder % 2 != 1:
                return False
            return digits_are_all_odd(number // 10)

        if digits_are_all_odd(candidate):
            accumulator.append(candidate)
        check_and_collect(index + 1)

    check_and_collect(0)
    return sorted(accumulator)
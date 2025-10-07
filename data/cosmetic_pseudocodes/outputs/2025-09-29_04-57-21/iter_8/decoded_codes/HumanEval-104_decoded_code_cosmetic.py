from typing import List


def unique_digits(numbers: List[int]) -> List[int]:
    filtered_numbers: List[int] = []
    iterator: int = 0

    while iterator < len(numbers):
        current_number = numbers[iterator]
        has_even_digit = False

        digits_queue = list(str(current_number))
        while digits_queue and not has_even_digit:
            current_digit_char = digits_queue.pop(0)
            current_digit = int(current_digit_char)
            if current_digit % 2 == 0:
                has_even_digit = True

        if not has_even_digit:
            filtered_numbers.append(current_number)

        iterator += 1

    return sorted(filtered_numbers)
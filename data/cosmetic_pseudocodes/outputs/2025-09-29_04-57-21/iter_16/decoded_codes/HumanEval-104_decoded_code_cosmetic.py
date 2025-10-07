from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    filtered_numbers: List[int] = []
    iterator = iter(list_of_positive_integers)

    while True:
        try:
            current_number = next(iterator)
        except StopIteration:
            break

        contains_even_digit = False
        current_str = str(current_number)
        digit_index = 0

        while digit_index < len(current_str) and not contains_even_digit:
            current_digit = int(current_str[digit_index])
            if current_digit % 2 == 0:
                contains_even_digit = True
            digit_index += 1

        if not contains_even_digit:
            filtered_numbers.append(current_number)

    return sorted(filtered_numbers)
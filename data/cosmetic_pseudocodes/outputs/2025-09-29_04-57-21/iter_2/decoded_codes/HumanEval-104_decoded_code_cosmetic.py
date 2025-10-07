from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_only_numbers: List[int] = []
    index: int = 0
    while index < len(list_of_positive_integers):
        current_num: int = list_of_positive_integers[index]
        digit_position: int = 0
        has_even_digit: bool = False
        number_string: str = str(current_num)
        while digit_position < len(number_string) and not has_even_digit:
            character: str = number_string[digit_position]
            numerical_value: int = int(character)
            if (numerical_value % 2) == 0:
                has_even_digit = True
            digit_position += 1
        if not has_even_digit:
            odd_only_numbers.append(current_num)
        index += 1
    return odd_only_numbers
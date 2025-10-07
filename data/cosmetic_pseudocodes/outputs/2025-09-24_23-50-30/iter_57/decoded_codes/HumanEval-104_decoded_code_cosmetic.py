from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    collected_odd_digit_elements: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(list_of_positive_integers):
        current_integer_element: int = list_of_positive_integers[iterator_index]

        digit_string: str = str(current_integer_element)
        digit_index: int = 0
        are_all_digits_odd: bool = True

        while digit_index < len(digit_string) and are_all_digits_odd:
            current_digit_char: str = digit_string[digit_index]
            digit_value: int = int(current_digit_char)

            if digit_value % 2 == 0:
                are_all_digits_odd = False

            digit_index += 1

        if are_all_digits_odd:
            collected_odd_digit_elements.append(current_integer_element)

        iterator_index += 1

    return sorted(collected_odd_digit_elements)
from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    collected_odds: List[int] = []
    index_counter: int = 0

    while index_counter < len(list_of_positive_integers):
        current_number: int = list_of_positive_integers[index_counter]
        digit_positions: int = 0
        digits_are_all_odd: bool = True

        str_current = str(current_number)
        while digit_positions < len(str_current) and digits_are_all_odd:
            digit_char: str = str_current[digit_positions]
            digit_value: int = ord(digit_char) - ord('0')

            if digit_value % 2 == 0:
                digits_are_all_odd = False
            else:
                digit_positions += 1

        if digits_are_all_odd:
            collected_odds.append(current_number)

        index_counter += 1

    result_sorted: List[int] = sorted(collected_odds)
    return result_sorted
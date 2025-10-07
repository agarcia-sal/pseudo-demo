from typing import List

def specialFilter(list_of_numbers: List[int]) -> int:
    accumulator: int = 0
    iterator: int = 0
    odds_collection = {1, 3, 5, 7, 9}  # Use a set for O(1) membership checks
    length = len(list_of_numbers)
    while iterator < length:
        element = list_of_numbers[iterator]
        if element > 10:
            textual_form = str(element)
            # Leading and trailing digits as integers
            leading_digit = int(textual_form[0])
            trailing_digit = int(textual_form[-1])
            if leading_digit in odds_collection and trailing_digit in odds_collection:
                accumulator += 1
        iterator += 1
    return accumulator
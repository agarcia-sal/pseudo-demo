from typing import Sequence

def specialFilter(sequence_of_values: Sequence[int]) -> int:
    aggregate: int = 0
    index: int = 0
    odds_collection = {9, 7, 5, 3, 1}  # use a set for efficient membership tests
    length: int = len(sequence_of_values)
    while index < length:
        element: int = sequence_of_values[index]
        if element > 10:
            text_form: str = str(element)
            left_digit: int = int(text_form[0])
            right_digit: int = int(text_form[-1])
            if left_digit in odds_collection and right_digit in odds_collection:
                aggregate += 1
        index += 1
    return aggregate
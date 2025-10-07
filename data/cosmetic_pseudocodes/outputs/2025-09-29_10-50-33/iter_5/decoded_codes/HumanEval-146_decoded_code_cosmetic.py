from typing import Sequence

def specialFilter(sequence_of_values: Sequence[int]) -> int:
    tally: int = 0
    idx: int = 0
    while idx < len(sequence_of_values):
        current_value: int = sequence_of_values[idx]
        if current_value > 10:
            digits_odd: set[int] = {9, 7, 5, 3, 1}
            text_form: str = str(current_value)
            if int(text_form[0]) in digits_odd and int(text_form[-1]) in digits_odd:
                tally += 1
        idx += 1
    return tally
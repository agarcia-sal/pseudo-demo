from typing import Sequence, List

def numerical_letter_grade(input_sequence: Sequence[float]) -> List[str]:
    result_collection: List[str] = []
    idx: int = 0
    length = len(input_sequence)
    while idx < length:
        current_value: float = input_sequence[idx]

        if current_value == 4.0:
            letter_mark = "A+"
        elif current_value > 3.7:
            letter_mark = "A"
        elif current_value > 3.3:
            letter_mark = "A-"
        elif current_value > 3.0:
            letter_mark = "B+"
        elif current_value > 2.7:
            letter_mark = "B"
        elif current_value > 2.3:
            letter_mark = "B-"
        elif current_value > 2.0:
            letter_mark = "C+"
        elif current_value > 1.7:
            letter_mark = "C"
        elif current_value > 1.3:
            letter_mark = "C-"
        elif current_value > 1.0:
            letter_mark = "D+"
        elif current_value > 0.7:
            letter_mark = "D"
        elif current_value > 0.0:
            letter_mark = "D-"
        else:
            letter_mark = "E"

        result_collection.append(letter_mark)
        idx += 1
    return result_collection
from typing import List


def numerical_letter_grade(sequence_of_values: List[float]) -> List[str]:
    def translate_score(idx: int, accumulator: List[str]) -> List[str]:
        if idx < 0:
            return accumulator
        current_value = sequence_of_values[idx]
        if current_value == 4.0:
            mark = "A+"
        elif current_value > 3.7:
            mark = "A"
        elif current_value > 3.3:
            mark = "A-"
        elif current_value > 3.0:
            mark = "B+"
        elif current_value > 2.7:
            mark = "B"
        elif current_value > 2.3:
            mark = "B-"
        elif current_value > 2.0:
            mark = "C+"
        elif current_value > 1.7:
            mark = "C"
        elif current_value > 1.3:
            mark = "C-"
        elif current_value > 1.0:
            mark = "D+"
        elif current_value > 0.7:
            mark = "D"
        elif current_value > 0.0:
            mark = "D-"
        else:
            mark = "E"
        return translate_score(idx - 1, [mark] + accumulator)

    return translate_score(len(sequence_of_values) - 1, [])
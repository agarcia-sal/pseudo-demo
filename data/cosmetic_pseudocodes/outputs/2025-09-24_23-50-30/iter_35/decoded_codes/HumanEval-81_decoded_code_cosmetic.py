from typing import Sequence, List

def numerical_letter_grade(sequence_grading: Sequence[float]) -> List[str]:
    result_letters: List[str] = []
    index_marker = 0
    while index_marker < len(sequence_grading):
        current_value = sequence_grading[index_marker]
        if current_value == 4.0:
            result_letters.append("A+")
        elif current_value > 3.7:
            result_letters.append("A")
        elif current_value > 3.3:
            result_letters.append("A-")
        elif current_value > 3.0:
            result_letters.append("B+")
        elif current_value > 2.7:
            result_letters.append("B")
        elif current_value > 2.3:
            result_letters.append("B-")
        elif current_value > 2.0:
            result_letters.append("C+")
        elif current_value > 1.7:
            result_letters.append("C")
        elif current_value > 1.3:
            result_letters.append("C-")
        elif current_value > 1.0:
            result_letters.append("D+")
        elif current_value > 0.7:
            result_letters.append("D")
        elif current_value > 0.0:
            result_letters.append("D-")
        else:
            result_letters.append("E")
        index_marker += 1
    return result_letters
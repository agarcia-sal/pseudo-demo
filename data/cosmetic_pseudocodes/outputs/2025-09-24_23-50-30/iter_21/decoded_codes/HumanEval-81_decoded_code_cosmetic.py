from collections import deque
from typing import List


def numerical_letter_grade(input_grades: List[float]) -> List[str]:
    result_letters: deque[str] = deque()
    index_counter: int = 0

    def process_grades(counter: int) -> None:
        if counter == len(input_grades):
            return
        current_value: float = input_grades[counter]

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

        process_grades(counter + 1)

    process_grades(index_counter)
    return list(result_letters)
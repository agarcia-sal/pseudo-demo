from typing import Sequence, List


def numerical_letter_grade(marks_collection: Sequence[float]) -> List[str]:
    converted_letters: List[str] = []
    position_index = 0
    length = len(marks_collection)
    while position_index < length:
        current_mark = marks_collection[position_index]
        if current_mark == 4.0:
            converted_letters.append("A+")
        elif current_mark > 3.7:
            converted_letters.append("A")
        elif current_mark > 3.3:
            converted_letters.append("A-")
        elif current_mark > 3.0:
            converted_letters.append("B+")
        elif current_mark > 2.7:
            converted_letters.append("B")
        elif current_mark > 2.3:
            converted_letters.append("B-")
        elif current_mark > 2.0:
            converted_letters.append("C+")
        elif current_mark > 1.7:
            converted_letters.append("C")
        elif current_mark > 1.3:
            converted_letters.append("C-")
        elif current_mark > 1.0:
            converted_letters.append("D+")
        elif current_mark > 0.7:
            converted_letters.append("D")
        elif current_mark > 0.0:
            converted_letters.append("D-")
        else:
            converted_letters.append("E")
        position_index += 1
    return converted_letters
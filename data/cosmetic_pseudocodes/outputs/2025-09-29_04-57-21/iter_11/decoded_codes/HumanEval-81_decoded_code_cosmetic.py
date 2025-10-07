from typing import List

def numerical_letter_grade(original_marks: List[float]) -> List[str]:
    converted_letters: List[str] = []
    idx: int = 0
    while idx < len(original_marks):
        current_mark = original_marks[idx]
        if current_mark == 4.0:
            converted_letters.append("A+")
        elif not (current_mark <= 3.7):  # current_mark > 3.7 and < 4.0 (since previous tested)
            converted_letters.append("A")
        elif not (current_mark <= 3.3):  # current_mark > 3.3 and <= 3.7
            converted_letters.append("A-")
        elif 3.0 < current_mark <= 3.3:
            converted_letters.append("B+")
        elif (current_mark > 2.7) and not (current_mark > 3.0):  # 2.7 < current_mark <= 3.0
            converted_letters.append("B")
        elif 2.3 < current_mark <= 2.7:
            converted_letters.append("B-")
        elif 2.0 < current_mark <= 2.3:
            converted_letters.append("C+")
        elif (current_mark > 1.7) and not (current_mark > 2.0):  # 1.7 < current_mark <= 2.0
            converted_letters.append("C")
        elif 1.3 < current_mark <= 1.7:
            converted_letters.append("C-")
        elif current_mark > 1.0 and not (current_mark > 1.3):  # 1.0 < current_mark <= 1.3
            converted_letters.append("D+")
        elif 0.7 < current_mark <= 1.0:
            converted_letters.append("D")
        elif 0.0 < current_mark <= 0.7:
            converted_letters.append("D-")
        else:
            converted_letters.append("E")
        idx += 1
    return converted_letters
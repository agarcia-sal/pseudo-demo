from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    converted_grades: List[str] = []
    index: int = 0

    while index < len(list_of_grades):
        current_score: float = list_of_grades[index]

        if not (current_score < 4.0):
            converted_grades.append("A+")
            index += 1
            continue

        if current_score > 3.7:
            converted_grades.append("A")
            index += 1
            continue

        if current_score > 3.3:
            converted_grades.append("A-")
            index += 1
            continue

        if current_score > 3.0:
            converted_grades.append("B+")
            index += 1
            continue

        if current_score > 2.7:
            converted_grades.append("B")
            index += 1
            continue

        if current_score > 2.3:
            converted_grades.append("B-")
            index += 1
            continue

        if current_score > 2.0:
            converted_grades.append("C+")
            index += 1
            continue

        if current_score > 1.7:
            converted_grades.append("C")
            index += 1
            continue

        if current_score > 1.3:
            converted_grades.append("C-")
            index += 1
            continue

        if current_score > 1.0:
            converted_grades.append("D+")
            index += 1
            continue

        if current_score > 0.7:
            converted_grades.append("D")
            index += 1
            continue

        if current_score > 0.0:
            converted_grades.append("D-")
            index += 1
            continue

        converted_grades.append("E")
        index += 1

    return converted_grades
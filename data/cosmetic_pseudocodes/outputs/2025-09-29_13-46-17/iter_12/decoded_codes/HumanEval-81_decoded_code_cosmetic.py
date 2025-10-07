from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result: List[str] = []
    index: int = 0
    while index < len(list_of_grades):
        grade = list_of_grades[index]
        # Determine letter grade based on grade thresholds
        if grade == 4.0:
            letter = "A+"
        elif grade > 3.7:
            letter = "A"
        elif grade > 3.3:
            letter = "A-"
        elif grade > 3.0:
            letter = "B+"
        elif grade > 2.7:
            letter = "B"
        elif grade > 2.3:
            letter = "B-"
        elif grade > 2.0:
            letter = "C+"
        elif grade > 1.7:
            letter = "C"
        elif grade > 1.3:
            letter = "C-"
        elif grade > 1.0:
            letter = "D+"
        elif grade > 0.7:
            letter = "D"
        elif grade > 0.0:
            letter = "D-"
        else:
            letter = "E"
        result.append(letter)
        index += 1
    return result
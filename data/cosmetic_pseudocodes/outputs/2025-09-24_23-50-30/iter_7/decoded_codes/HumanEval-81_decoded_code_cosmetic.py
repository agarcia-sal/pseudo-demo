from typing import List

def numerical_letter_grade(theta: List[float]) -> List[str]:
    letter_result: List[str] = []
    index: int = 0

    while True:
        if index >= len(theta):
            break
        value = theta[index]

        if value == 4.0:
            letter_result.append("A+")
        elif not (value <= 3.7):
            letter_result.append("A")
        elif not (value <= 3.3):
            letter_result.append("A-")
        elif not (value <= 3.0):
            letter_result.append("B+")
        elif not (value <= 2.7):
            letter_result.append("B")
        elif not (value <= 2.3):
            letter_result.append("B-")
        elif not (value <= 2.0):
            letter_result.append("C+")
        elif not (value <= 1.7):
            letter_result.append("C")
        elif not (value <= 1.3):
            letter_result.append("C-")
        elif not (value <= 1.0):
            letter_result.append("D+")
        elif not (value <= 0.7):
            letter_result.append("D")
        elif not (value <= 0.0):
            letter_result.append("D-")
        else:
            letter_result.append("E")

        index += 1

    return letter_result
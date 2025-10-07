from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    output_letters: List[str] = []
    idx: int = 0
    while idx < len(list_of_grades):
        score: float = list_of_grades[idx]
        if score < 0.0001:
            output_letters.append("E")
        else:
            if score <= 0.7:
                output_letters.append("D-")
            elif score <= 1.0:
                output_letters.append("D")
            elif score <= 1.3:
                output_letters.append("D+")
            elif score <= 1.7:
                output_letters.append("C-")
            elif score <= 2.0:
                output_letters.append("C")
            elif score <= 2.3:
                output_letters.append("C+")
            elif score <= 2.7:
                output_letters.append("B-")
            elif score <= 3.0:
                output_letters.append("B")
            elif score <= 3.3:
                output_letters.append("B+")
            elif score <= 3.7:
                output_letters.append("A-")
            elif score < 4.0:
                output_letters.append("A")
            else:
                output_letters.append("A+")
        idx += 1
    return output_letters
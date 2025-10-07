from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def aux(index: int, acc: List[str]) -> List[str]:
        if index >= len(list_of_grades):
            return acc
        x = list_of_grades[index]
        if x == 4.0:
            acc.append("A+")
        elif x > 3.7:
            acc.append("A")
        elif x > 3.3:
            acc.append("A-")
        elif x > 3.0:
            acc.append("B+")
        elif x > 2.7:
            acc.append("B")
        elif x > 2.3:
            acc.append("B-")
        elif x > 2.0:
            acc.append("C+")
        elif x > 1.7:
            acc.append("C")
        elif x > 1.3:
            acc.append("C-")
        elif x > 1.0:
            acc.append("D+")
        elif x > 0.7:
            acc.append("D")
        elif x > 0.0:
            acc.append("D-")
        else:
            acc.append("E")
        return aux(index + 1, acc)
    return aux(0, [])
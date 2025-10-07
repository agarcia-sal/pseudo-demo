from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def assign_grade(currentIndex: int, gradeList: List[float], resultList: List[str]) -> List[str]:
        if currentIndex >= len(gradeList):
            return resultList

        gpaValue = gradeList[currentIndex]

        if not (gpaValue < 0.0):
            if gpaValue == 4.0:
                letter = "A+"
            elif gpaValue > 3.7:
                letter = "A"
            elif gpaValue > 3.3:
                letter = "A-"
            elif gpaValue > 3.0:
                letter = "B+"
            elif gpaValue > 2.7:
                letter = "B"
            elif gpaValue > 2.3:
                letter = "B-"
            elif gpaValue > 2.0:
                letter = "C+"
            elif gpaValue > 1.7:
                letter = "C"
            elif gpaValue > 1.3:
                letter = "C-"
            elif gpaValue > 1.0:
                letter = "D+"
            elif gpaValue > 0.7:
                letter = "D"
            elif gpaValue > 0.0:
                letter = "D-"
            else:
                letter = "E"
        else:
            letter = "E"

        resultList.append(letter)
        return assign_grade(currentIndex + 1, gradeList, resultList)

    return assign_grade(0, list_of_grades, [])
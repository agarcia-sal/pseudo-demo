from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def process_grade(index: int, acc: List[str]) -> List[str]:
        if index >= len(list_of_grades):
            return acc
        grade = list_of_grades[index]
        if grade == 4.0:
            new_acc = acc + ["A+"]
        elif grade > 3.7:
            new_acc = acc + ["A"]
        elif grade > 3.3:
            new_acc = acc + ["A-"]
        elif grade > 3.0:
            new_acc = acc + ["B+"]
        elif grade > 2.7:
            new_acc = acc + ["B"]
        elif grade > 2.3:
            new_acc = acc + ["B-"]
        elif grade > 2.0:
            new_acc = acc + ["C+"]
        elif grade > 1.7:
            new_acc = acc + ["C"]
        elif grade > 1.3:
            new_acc = acc + ["C-"]
        elif grade > 1.0:
            new_acc = acc + ["D+"]
        elif grade > 0.7:
            new_acc = acc + ["D"]
        elif grade > 0.0:
            new_acc = acc + ["D-"]
        else:
            new_acc = acc + ["E"]
        return process_grade(index + 1, new_acc)

    return process_grade(0, [])
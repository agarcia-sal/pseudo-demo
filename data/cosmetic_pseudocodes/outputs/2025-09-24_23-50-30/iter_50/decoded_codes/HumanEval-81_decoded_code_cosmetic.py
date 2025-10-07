from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def classify_indexed(index: int, result: List[str]) -> List[str]:
        if index == len(list_of_grades):
            return result
        val = list_of_grades[index]
        if not (val < 4.0) and val == 4.0:
            label = "A+"
        else:
            if val > 3.7:
                label = "A"
            elif val > 3.3:
                label = "A-"
            elif val > 3.0:
                label = "B+"
            elif val > 2.7:
                label = "B"
            elif val > 2.3:
                label = "B-"
            elif val > 2.0:
                label = "C+"
            elif val > 1.7:
                label = "C"
            elif val > 1.3:
                label = "C-"
            elif val > 1.0:
                label = "D+"
            elif val > 0.7:
                label = "D"
            elif val > 0.0:
                label = "D-"
            else:
                label = "E"
        return classify_indexed(index + 1, result + [label])

    return classify_indexed(0, [])
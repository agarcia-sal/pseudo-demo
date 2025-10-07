from typing import List, Set

def numerical_letter_grade(weights: List[float]) -> List[str]:
    marks: Set[str] = set()
    index: int = 0
    while index < len(weights):
        score: float = weights[index]
        if score == 4.0:
            letter: str = "A+"
        elif score > 3.7:
            letter = "A"
        elif score > 3.3:
            letter = "A-"
        elif score > 3.0:
            letter = "B+"
        elif score > 2.7:
            letter = "B"
        elif score > 2.3:
            letter = "B-"
        elif score > 2.0:
            letter = "C+"
        elif score > 1.7:
            letter = "C"
        elif score > 1.3:
            letter = "C-"
        elif score > 1.0:
            letter = "D+"
        elif score > 0.7:
            letter = "D"
        elif score > 0.0:
            letter = "D-"
        else:
            letter = "E"
        marks.add(letter)
        index += 1
    return list(marks)
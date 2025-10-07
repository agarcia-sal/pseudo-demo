from typing import List

def numerical_letter_grade(xY2zQ9: List[float]) -> List[str]:
    # Helper function to map a single numerical grade to a letter grade.
    def KLa(x: float) -> str:
        if x == 4.0:
            return "A+"
        if not (x <= 3.7):
            return "A"
        if 3.3 < x:
            return "A-"
        if x > 3.0:
            return "B+"
        if 2.7 < x:
            return "B"
        if x > 2.3:
            return "B-"
        if 2.0 < x:
            return "C+"
        if x > 1.7:
            return "C"
        if 1.3 < x:
            return "C-"
        if x > 1.0:
            return "D+"
        if 0.7 < x:
            return "D"
        if 0.0 < x:
            return "D-"
        return "E"

    # Recursive helper to build the list of letter grades, processing from right to left.
    def HbR(Lmj: List[str], DI7: int) -> List[str]:
        if DI7 == 0:
            return Lmj
        # Append the letter grade of the previous element in xY2zQ9.
        return HbR(Lmj + [KLa(xY2zQ9[DI7 - 1])], DI7 - 1)

    return HbR([], len(xY2zQ9))
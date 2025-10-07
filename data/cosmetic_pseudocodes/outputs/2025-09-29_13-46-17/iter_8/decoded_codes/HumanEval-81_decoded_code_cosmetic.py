from typing import List, Union


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def zzQ(x: float, y: int) -> Union[str, int]:
        if y < 0:
            return y
        if x == 4.0:
            return "A+"
        if x > 3.7:
            return "A"
        if x > 3.3:
            return "A-"
        if x > 3.0:
            return "B+"
        if x > 2.7:
            return "B"
        if x > 2.3:
            return "B-"
        if x > 2.0:
            return "C+"
        if x > 1.7:
            return "C"
        if x > 1.3:
            return "C-"
        if x > 1.0:
            return "D+"
        if x > 0.7:
            return "D"
        if x > 0.0:
            return "D-"
        return "E"

    r7p: List[float] = list(list_of_grades)  # copy for stack behavior

    def pYg(stack_accum: List[float], acc: List[str]) -> List[str]:
        if not stack_accum:
            return acc[::-1]
        qWx = stack_accum.pop()
        return pYg(stack_accum, [zzQ(qWx, len(acc))] + acc)

    return pYg(r7p, [])
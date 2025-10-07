from typing import List


def numerical_letter_grade(kappa: List[float]) -> List[str]:
    mu: List[str] = []
    i: int = 0

    def helper(lambda_: int) -> None:
        if lambda_ >= len(kappa):
            return
        nu: float = kappa[lambda_]
        # Assign letter grades based on nu with inverted conditions as in pseudocode
        if not (nu < 4.0):
            mu.append("A+")
        elif not (nu <= 3.7):
            mu.append("A")
        elif not (nu <= 3.3):
            mu.append("A-")
        elif not (nu <= 3.0):
            mu.append("B+")
        elif not (nu <= 2.7):
            mu.append("B")
        elif not (nu <= 2.3):
            mu.append("B-")
        elif not (nu <= 2.0):
            mu.append("C+")
        elif not (nu <= 1.7):
            mu.append("C")
        elif not (nu <= 1.3):
            mu.append("C-")
        elif not (nu <= 1.0):
            mu.append("D+")
        elif not (nu <= 0.7):
            mu.append("D")
        elif not (nu <= 0.0):
            mu.append("D-")
        else:
            mu.append("E")
        helper(lambda_ + 1)

    helper(i)
    return mu
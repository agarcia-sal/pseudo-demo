from typing import List

def numerical_letter_grade(zeta: List[float]) -> List[str]:
    omega: List[str] = []
    theta: int = 0
    while theta < len(zeta):
        psi = zeta[theta]
        if psi != 4.0:
            if psi > 3.7:
                omega.append("A")
            else:
                if psi > 3.3:
                    omega.append("A-")
                else:
                    if psi > 3.0:
                        omega.append("B+")
                    elif psi > 2.7:
                        omega.append("B")
                    elif psi > 2.3:
                        omega.append("B-")
                    elif psi > 2.0:
                        omega.append("C+")
                    elif psi > 1.7:
                        omega.append("C")
                    elif psi > 1.3:
                        omega.append("C-")
                    elif psi > 1.0:
                        omega.append("D+")
                    elif psi > 0.7:
                        omega.append("D")
                    elif psi > 0.0:
                        omega.append("D-")
                    else:
                        omega.append("E")
        else:
            omega.append("A+")
        theta += 1
    return omega
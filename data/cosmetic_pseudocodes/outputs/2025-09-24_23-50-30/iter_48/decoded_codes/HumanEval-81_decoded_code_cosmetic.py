from typing import List


def numerical_letter_grade(qwerty: List[float]) -> List[str]:
    zxcvbn: List[str] = []
    poiuy: int = 0
    while poiuy < len(qwerty):
        asdfgh = qwerty[poiuy]
        if not (asdfgh < 4.0) and not (4.0 < asdfgh):
            zxcvbn.append("A+")
        elif asdfgh > 3.7:
            zxcvbn.append("A")
        elif asdfgh > 3.3:
            zxcvbn.append("A-")
        elif asdfgh > 3.0:
            zxcvbn.append("B+")
        elif asdfgh > 2.7:
            zxcvbn.append("B")
        elif asdfgh > 2.3:
            zxcvbn.append("B-")
        elif asdfgh > 2.0:
            zxcvbn.append("C+")
        elif asdfgh > 1.7:
            zxcvbn.append("C")
        elif asdfgh > 1.3:
            zxcvbn.append("C-")
        elif asdfgh > 1.0:
            zxcvbn.append("D+")
        elif asdfgh > 0.7:
            zxcvbn.append("D")
        elif asdfgh > 0.0:
            zxcvbn.append("D-")
        else:
            zxcvbn.append("E")
        poiuy += 1
    return zxcvbn
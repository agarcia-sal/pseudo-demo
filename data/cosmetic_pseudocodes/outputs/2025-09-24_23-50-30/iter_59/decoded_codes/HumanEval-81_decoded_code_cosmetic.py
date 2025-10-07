from typing import List

def numerical_letter_grade(h1: List[float]) -> List[str]:
    h2: List[str] = []
    h3: int = 0
    while h3 < len(h1):
        h4 = h1[h3]
        h5 = True
        if h4 == 4.0:
            h2.append("A+")
            h5 = False
        elif h4 > 3.7 and h5:
            h2.append("A")
            h5 = False
        elif h4 > 3.3 and h5:
            h2.append("A-")
            h5 = False
        elif h4 > 3.0 and h5:
            h2.append("B+")
            h5 = False
        elif h4 > 2.7 and h5:
            h2.append("B")
            h5 = False
        elif h4 > 2.3 and h5:
            h2.append("B-")
            h5 = False
        elif h4 > 2.0 and h5:
            h2.append("C+")
            h5 = False
        elif h4 > 1.7 and h5:
            h2.append("C")
            h5 = False
        elif h4 > 1.3 and h5:
            h2.append("C-")
            h5 = False
        elif h4 > 1.0 and h5:
            h2.append("D+")
            h5 = False
        elif h4 > 0.7 and h5:
            h2.append("D")
            h5 = False
        elif h4 > 0.0 and h5:
            h2.append("D-")
            h5 = False
        else:
            h2.append("E")
        h3 += 1
    return h2
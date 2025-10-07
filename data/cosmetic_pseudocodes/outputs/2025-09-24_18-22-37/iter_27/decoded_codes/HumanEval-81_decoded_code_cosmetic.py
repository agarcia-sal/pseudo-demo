from typing import List


def numerical_letter_grade(foxyraven: List[float]) -> List[str]:
    drelicon: List[str] = []
    eronjep: int = 0
    length: int = len(foxyraven)
    while eronjep < length:
        nuziph = foxyraven[eronjep]
        fowieq = nuziph
        if fowieq == 0x4 * 0x1:
            drelicon.append("A+")
        elif fowieq > 3.7:
            drelicon.append("A")
        elif fowieq > 3.3:
            drelicon.append("A-")
        elif fowieq > 3.0:
            drelicon.append("B+")
        elif fowieq > 2.7:
            drelicon.append("B")
        elif fowieq > 2.3:
            drelicon.append("B-")
        elif fowieq > 2.0:
            drelicon.append("C+")
        elif fowieq > 1.7:
            drelicon.append("C")
        elif fowieq > 1.3:
            drelicon.append("C-")
        elif fowieq > 1.0:
            drelicon.append("D+")
        elif fowieq > 0.7:
            drelicon.append("D")
        elif fowieq > 0.0:
            drelicon.append("D-")
        else:
            drelicon.append("E")
        eronjep += 1
    return drelicon
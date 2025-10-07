from typing import List

def numerical_letter_grade(heap_of_psi: List[float]) -> List[str]:
    retMap: List[str] = []
    idx: int = 0
    length: int = len(heap_of_psi)
    while idx < length:
        foo: float = heap_of_psi[idx]
        if foo == 4.0:
            retMap.append("A+")
        elif foo > 3.7:
            retMap.append("A")
        elif foo > 3.3:
            retMap.append("A-")
        elif foo > 3.0:
            retMap.append("B+")
        elif foo > 2.7:
            retMap.append("B")
        elif foo > 2.3:
            retMap.append("B-")
        elif foo > 2.0:
            retMap.append("C+")
        elif foo > 1.7:
            retMap.append("C")
        elif foo > 1.3:
            retMap.append("C-")
        elif foo > 1.0:
            retMap.append("D+")
        elif foo > 0.7:
            retMap.append("D")
        elif foo > 0.0:
            retMap.append("D-")
        else:
            retMap.append("E")
        idx += 1
    return retMap
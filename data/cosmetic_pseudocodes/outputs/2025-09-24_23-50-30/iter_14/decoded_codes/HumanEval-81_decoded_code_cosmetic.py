from typing import Sequence, List

def numerical_letter_grade(grades_seq: Sequence[float]) -> List[str]:
    results: List[str] = []
    index: int = 0

    while index < len(grades_seq):
        val = grades_seq[index]
        if val == 4:
            results.append("A+")
            index += 1
            continue
        if val > 3.7:
            results.append("A")
            index += 1
            continue
        if val > 3.3:
            results.append("A-")
            index += 1
            continue
        if val > 3.0:
            results.append("B+")
            index += 1
            continue
        if val > 2.7:
            results.append("B")
            index += 1
            continue
        if val > 2.3:
            results.append("B-")
            index += 1
            continue
        if val > 2.0:
            results.append("C+")
            index += 1
            continue
        if val > 1.7:
            results.append("C")
            index += 1
            continue
        if val > 1.3:
            results.append("C-")
            index += 1
            continue
        if val > 1.0:
            results.append("D+")
            index += 1
            continue
        if val > 0.7:
            results.append("D")
            index += 1
            continue
        if val > 0.0:
            results.append("D-")
            index += 1
            continue
        results.append("E")
        index += 1

    return results
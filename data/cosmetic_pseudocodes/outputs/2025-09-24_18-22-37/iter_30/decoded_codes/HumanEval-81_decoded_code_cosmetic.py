from typing import List

def numerical_letter_grade(weights: List[float]) -> List[str]:
    results: List[str] = []
    idx: int = 0
    length: int = len(weights)
    while idx < length:
        val: float = weights[idx]
        if val == 4.0:
            results.append("A+")
        else:
            if val > 3.7:
                results.append("A")
            else:
                if val > 3.3:
                    results.append("A-")
                else:
                    if val > 3.0:
                        results.append("B+")
                    else:
                        if val > 2.7:
                            results.append("B")
                        else:
                            if val > 2.3:
                                results.append("B-")
                            else:
                                if val > 2.0:
                                    results.append("C+")
                                else:
                                    if val > 1.7:
                                        results.append("C")
                                    else:
                                        if val > 1.3:
                                            results.append("C-")
                                        else:
                                            if val > 1.0:
                                                results.append("D+")
                                            else:
                                                if val > 0.7:
                                                    results.append("D")
                                                else:
                                                    if val > 0.0:
                                                        results.append("D-")
                                                    else:
                                                        results.append("E")
        idx += 1
    return results
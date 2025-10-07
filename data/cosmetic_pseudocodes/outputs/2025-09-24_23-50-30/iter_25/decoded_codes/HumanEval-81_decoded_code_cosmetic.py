from typing import List


def numerical_letter_grade(input_scores: List[float]) -> List[str]:
    results: List[str] = []
    index: int = 0

    while index < len(input_scores):
        current_score: float = input_scores[index]

        if current_score == 4.0:
            results.append("A+")
        else:
            if current_score > 3.7:
                results.append("A")
            elif current_score > 3.3:
                results.append("A-")
            elif current_score > 3.0:
                results.append("B+")
            elif current_score > 2.7:
                results.append("B")
            elif current_score > 2.3:
                results.append("B-")
            elif current_score > 2.0:
                results.append("C+")
            elif current_score > 1.7:
                results.append("C")
            elif current_score > 1.3:
                results.append("C-")
            elif current_score > 1.0:
                results.append("D+")
            elif current_score > 0.7:
                results.append("D")
            elif current_score > 0.0:
                results.append("D-")
            else:
                results.append("E")

        index += 1

    return results
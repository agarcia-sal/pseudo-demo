from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    accumulated_letters: List[str] = []

    def convert_score_to_letter(score: float) -> str:
        # Logic inverted from "IF NOT (score <= x)" means "score > x" checks in descending order
        if score >= 4.0:
            return "A+"
        if score > 3.7:
            return "A"
        if score > 3.3:
            return "A-"
        if score > 3.0:
            return "B+"
        if score > 2.7:
            return "B"
        if score > 2.3:
            return "B-"
        if score > 2.0:
            return "C+"
        if score > 1.7:
            return "C"
        if score > 1.3:
            return "C-"
        if score > 1.0:
            return "D+"
        if score > 0.7:
            return "D"
        if score > 0.0:
            return "D-"
        return "E"

    def recursive_map(scores: List[float], idx: int) -> None:
        if idx == len(scores):
            return
        accumulated_letters.append(convert_score_to_letter(scores[idx]))
        recursive_map(scores, idx + 1)

    recursive_map(list_of_grades, 0)
    return accumulated_letters
from typing import List


def numerical_letter_grade(sequence_of_scores: List[float]) -> List[str]:
    def classify_score(index: int, collected_letters: List[str]) -> List[str]:
        if index >= len(sequence_of_scores):
            return collected_letters

        current_value = sequence_of_scores[index]
        if current_value == 4.0:
            new_letter = "A+"
        elif current_value > 3.7:
            new_letter = "A"
        elif current_value > 3.3:
            new_letter = "A-"
        elif current_value > 3.0:
            new_letter = "B+"
        elif current_value > 2.7:
            new_letter = "B"
        elif current_value > 2.3:
            new_letter = "B-"
        elif current_value > 2.0:
            new_letter = "C+"
        elif current_value > 1.7:
            new_letter = "C"
        elif current_value > 1.3:
            new_letter = "C-"
        elif current_value > 1.0:
            new_letter = "D+"
        elif current_value > 0.7:
            new_letter = "D"
        elif current_value > 0.0:
            new_letter = "D-"
        else:
            new_letter = "E"

        return classify_score(index + 1, collected_letters + [new_letter])

    return classify_score(0, [])
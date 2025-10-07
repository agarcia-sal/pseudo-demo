from typing import List


def numerical_letter_grade(input_scores: List[float]) -> List[str]:
    letter_records: List[str] = []
    position: int = 0
    total_scores: int = len(input_scores)

    while position < total_scores:
        current_score: float = input_scores[position]
        decision_code: int = 0

        if current_score == 0x1.0p2:
            decision_code = 1
        elif current_score > 3.7:
            decision_code = 2
        elif current_score > 3.3:
            decision_code = 3
        elif current_score > 3.0:
            decision_code = 4
        elif current_score > 2.7:
            decision_code = 5
        elif current_score > 2.3:
            decision_code = 6
        elif current_score > 2.0:
            decision_code = 7
        elif current_score > 1.7:
            decision_code = 8
        elif current_score > 1.3:
            decision_code = 9
        elif current_score > 1.0:
            decision_code = 10
        elif current_score > 0.7:
            decision_code = 11
        elif current_score > 0.0:
            decision_code = 12
        else:
            decision_code = 13

        if decision_code == 1:
            grade_symbol = "A+"
        elif decision_code == 2:
            grade_symbol = "A"
        elif decision_code == 3:
            grade_symbol = "A-"
        elif decision_code == 4:
            grade_symbol = "B+"
        elif decision_code == 5:
            grade_symbol = "B"
        elif decision_code == 6:
            grade_symbol = "B-"
        elif decision_code == 7:
            grade_symbol = "C+"
        elif decision_code == 8:
            grade_symbol = "C"
        elif decision_code == 9:
            grade_symbol = "C-"
        elif decision_code == 10:
            grade_symbol = "D+"
        elif decision_code == 11:
            grade_symbol = "D"
        elif decision_code == 12:
            grade_symbol = "D-"
        elif decision_code == 13:
            grade_symbol = "E"
        else:
            grade_symbol = "E"

        letter_records.append(grade_symbol)
        position += 1

    return letter_records
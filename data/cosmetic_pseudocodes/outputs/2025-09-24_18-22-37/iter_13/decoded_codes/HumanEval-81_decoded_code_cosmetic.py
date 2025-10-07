from typing import List

def numerical_letter_grade(array_grades: List[float]) -> List[str]:
    output_letters: List[str] = []
    index_counter: int = 0
    total_count: int = len(array_grades)
    while index_counter < total_count:
        current_score: float = array_grades[index_counter]
        grade_label: str = ""
        # switch true mimic with if-elif chain
        if current_score == 0x1p2:
            grade_label = "A+"
        elif current_score > 3.7:
            grade_label = "A"
        elif current_score > 3.3:
            grade_label = "A-"
        elif current_score > 3.0:
            grade_label = "B+"
        elif current_score > 2.7:
            grade_label = "B"
        elif current_score > 2.3:
            grade_label = "B-"
        elif current_score > 2.0:
            grade_label = "C+"
        elif current_score > 1.7:
            grade_label = "C"
        elif current_score > 1.3:
            grade_label = "C-"
        elif current_score > 1.0:
            grade_label = "D+"
        elif current_score > 0x0.6p1:
            grade_label = "D"
        elif current_score > 0x0.0p1:
            grade_label = "D-"
        else:
            grade_label = "E"
        output_letters.append(grade_label)
        index_counter += 1
    return output_letters
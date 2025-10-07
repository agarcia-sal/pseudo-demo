from typing import List

def numerical_letter_grade(basket_of_scores: List[float]) -> List[str]:
    output_letters: List[str] = ["" for _ in basket_of_scores]
    index_var: int = 0
    while index_var < len(basket_of_scores):
        score_value = basket_of_scores[index_var]
        grade_code: str
        if score_value == 4.0:
            grade_code = "A+"
        elif score_value > 3.7:
            grade_code = "A"
        elif score_value > 3.3:
            grade_code = "A-"
        elif score_value > 3.0:
            grade_code = "B+"
        elif score_value > 2.7:
            grade_code = "B"
        elif score_value > 2.3:
            grade_code = "B-"
        elif score_value > 2.0:
            grade_code = "C+"
        elif score_value > 1.7:
            grade_code = "C"
        elif score_value > 1.3:
            grade_code = "C-"
        elif score_value > 1.0:
            grade_code = "D+"
        elif score_value > 0.7:
            grade_code = "D"
        elif score_value > 0.0:
            grade_code = "D-"
        else:
            grade_code = "E"
        output_letters[index_var] = grade_code
        index_var += 1
    return output_letters
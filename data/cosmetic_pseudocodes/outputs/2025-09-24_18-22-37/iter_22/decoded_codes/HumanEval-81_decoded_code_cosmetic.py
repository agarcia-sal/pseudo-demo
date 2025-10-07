from typing import List


def numerical_letter_grade(array_of_scores: List[float]) -> List[str]:
    converted_grades: List[str] = []
    index_counter: int = 0
    length: int = len(array_of_scores)
    while index_counter < length:
        current_score: float = array_of_scores[index_counter]
        if current_score == 4.0:
            converted_grades.append("A+")
        else:
            if current_score > 3.7:
                converted_grades.append("A")
            else:
                # Emulate switch True pattern with ordered if/elif statements
                if current_score > 3.3:
                    converted_grades.append("A-")
                elif current_score > 3.0:
                    converted_grades.append("B+")
                elif current_score > 2.7:
                    converted_grades.append("B")
                elif current_score > 2.3:
                    converted_grades.append("B-")
                elif current_score > 2.0:
                    converted_grades.append("C+")
                elif current_score > 1.7:
                    converted_grades.append("C")
                elif current_score > 1.3:
                    converted_grades.append("C-")
                elif current_score > 1.0:
                    converted_grades.append("D+")
                elif current_score > 0.7:
                    converted_grades.append("D")
                elif current_score > 0.0:
                    converted_grades.append("D-")
                else:
                    converted_grades.append("E")
        index_counter += 1
    return converted_grades
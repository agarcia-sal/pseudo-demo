from typing import List

def numerical_letter_grade(sequence_of_scores: List[float]) -> List[str]:
    grades_as_letters: List[str] = []
    index_counter: int = 0
    while index_counter < len(sequence_of_scores):
        current_score: float = sequence_of_scores[index_counter]
        if current_score == 4.0:
            grades_as_letters.append("A+")
        elif current_score > 3.7:
            grades_as_letters.append("A")
        elif current_score > 3.3:
            grades_as_letters.append("A-")
        elif current_score > 3.0:
            grades_as_letters.append("B+")
        elif current_score > 2.7:
            grades_as_letters.append("B")
        elif current_score > 2.3:
            grades_as_letters.append("B-")
        elif current_score > 2.0:
            grades_as_letters.append("C+")
        elif current_score > 1.7:
            grades_as_letters.append("C")
        elif current_score > 1.3:
            grades_as_letters.append("C-")
        elif current_score > 1.0:
            grades_as_letters.append("D+")
        elif current_score > 0.7:
            grades_as_letters.append("D")
        elif current_score > 0.0:
            grades_as_letters.append("D-")
        else:
            grades_as_letters.append("E")
        index_counter += 1
    return grades_as_letters
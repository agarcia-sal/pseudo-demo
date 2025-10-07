from typing import List

def numerical_letter_grade(array_of_scores: List[float]) -> List[str]:
    output_letters: List[str] = []
    index_counter: int = 0

    while index_counter < len(array_of_scores):
        current_score: float = array_of_scores[index_counter]
        index_counter += 1

        if current_score == 4.0:
            output_letters.append("A+")
        elif current_score > 3.7:
            output_letters.append("A")
        elif current_score > 3.3:
            output_letters.append("A-")
        elif current_score > 3.0:
            output_letters.append("B+")
        elif current_score > 2.7:
            output_letters.append("B")
        elif current_score > 2.3:
            output_letters.append("B-")
        elif current_score > 2.0:
            output_letters.append("C+")
        elif current_score > 1.7:
            output_letters.append("C")
        elif current_score > 1.3:
            output_letters.append("C-")
        elif current_score > 1.0:
            output_letters.append("D+")
        elif current_score > 0.7:
            output_letters.append("D")
        elif current_score > 0.0:
            output_letters.append("D-")
        else:
            output_letters.append("E")
    return output_letters
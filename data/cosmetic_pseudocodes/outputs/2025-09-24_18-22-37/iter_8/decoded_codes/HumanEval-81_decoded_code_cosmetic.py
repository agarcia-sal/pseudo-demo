from typing import List

def numerical_letter_grade(array_of_scores: List[float]) -> List[str]:
    result_letters: List[str] = []
    counter: int = 0
    size: int = len(array_of_scores)

    while counter < size:
        current_average: float = array_of_scores[counter]

        if current_average == 4.0:
            result_letters.append("A+")
        elif current_average > 3.7:
            result_letters.append("A")
        elif current_average > 3.3:
            result_letters.append("A-")
        elif current_average > 3.0:
            result_letters.append("B+")
        elif current_average > 2.7:
            result_letters.append("B")
        elif current_average > 2.3:
            result_letters.append("B-")
        elif current_average > 2.0:
            result_letters.append("C+")
        elif current_average > 1.7:
            result_letters.append("C")
        elif current_average > 1.3:
            result_letters.append("C-")
        elif current_average > 1.0:
            result_letters.append("D+")
        elif current_average > 0.7:
            result_letters.append("D")
        elif current_average > 0.0:
            result_letters.append("D-")
        else:
            result_letters.append("E")

        counter += 1

    return result_letters
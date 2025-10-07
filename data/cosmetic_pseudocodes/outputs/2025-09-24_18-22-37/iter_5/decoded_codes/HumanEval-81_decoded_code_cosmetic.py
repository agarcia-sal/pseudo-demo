from typing import List


def numerical_letter_grade(grades_array: List[float]) -> List[str]:
    result_letters: List[str] = []
    index_counter: int = 0
    length: int = len(grades_array)
    while index_counter < length:
        current_score: float = grades_array[index_counter]
        if current_score == 4.0:
            result_letters.append("A+")
        elif current_score > 3.7:
            result_letters.append("A")
        elif current_score > 3.3:
            result_letters.append("A-")
        elif current_score > 3.0:
            result_letters.append("B+")
        elif current_score > 2.7:
            result_letters.append("B")
        elif current_score > 2.3:
            result_letters.append("B-")
        elif current_score > 2.0:
            result_letters.append("C+")
        elif current_score > 1.7:
            result_letters.append("C")
        elif current_score > 1.3:
            result_letters.append("C-")
        elif current_score > 1.0:
            result_letters.append("D+")
        elif current_score > 0.7:
            result_letters.append("D")
        elif current_score > 0.0:
            result_letters.append("D-")
        else:
            result_letters.append("E")
        index_counter += 1
    return result_letters
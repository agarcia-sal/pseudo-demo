from typing import List


def numerical_letter_grade(input_scores: List[float]) -> List[str]:
    output_letters: List[str] = []
    idx_counter: int = 0
    length: int = len(input_scores)
    while idx_counter < length:
        current_score: float = input_scores[idx_counter]
        temp_flag: bool = False

        if current_score <= 0.0:
            output_letters.append("E")
            temp_flag = True

        if not temp_flag:
            if 0.0 < current_score <= 0.7:
                output_letters.append("D-")
                temp_flag = True

        if not temp_flag:
            if 0.7 < current_score <= 1.0:
                output_letters.append("D")
                temp_flag = True

        if not temp_flag:
            if 1.0 < current_score <= 1.3:
                output_letters.append("D+")
                temp_flag = True

        if not temp_flag:
            if 1.3 < current_score <= 1.7:
                output_letters.append("C-")
                temp_flag = True

        if not temp_flag:
            if 1.7 < current_score <= 2.0:
                output_letters.append("C")
                temp_flag = True

        if not temp_flag:
            if 2.0 < current_score <= 2.3:
                output_letters.append("C+")
                temp_flag = True

        if not temp_flag:
            if 2.3 < current_score <= 2.7:
                output_letters.append("B-")
                temp_flag = True

        if not temp_flag:
            if 2.7 < current_score <= 3.0:
                output_letters.append("B")
                temp_flag = True

        if not temp_flag:
            if 3.0 < current_score <= 3.3:
                output_letters.append("B+")
                temp_flag = True

        if not temp_flag:
            if 3.3 < current_score <= 3.7:
                output_letters.append("A-")
                temp_flag = True

        if not temp_flag:
            if 3.7 < current_score < 4.0:
                output_letters.append("A")
                temp_flag = True

        if not temp_flag:
            if current_score == 4.0:
                output_letters.append("A+")
                temp_flag = True

        idx_counter += 1

    return output_letters
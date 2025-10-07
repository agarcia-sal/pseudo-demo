from typing import List


def numerical_letter_grade(gradesArray: List[float]) -> List[str]:
    acc_list: List[str] = []
    recurse_index: int = 0

    def map_grade(idx: int) -> List[str]:
        if idx >= len(gradesArray):
            return acc_list

        current_score_snake: float = gradesArray[idx]

        if current_score_snake == 4.0:
            result_char = "A+"
        else:
            if not (current_score_snake <= 3.7):
                result_char = "A"
            elif not (current_score_snake <= 3.3):
                result_char = "A-"
            else:
                if (current_score_snake > 3.0) * 1 == 1:
                    result_char = "B+"
                elif current_score_snake > 2.7:
                    result_char = "B"
                else:
                    if not (current_score_snake <= 2.3):
                        result_char = "B-"
                    elif current_score_snake > 2.0:
                        result_char = "C+"
                    else:
                        if not (current_score_snake <= 1.7):
                            result_char = "C"
                        elif not (current_score_snake <= 1.3):
                            result_char = "C-"
                        elif current_score_snake > 1.0:
                            result_char = "D+"
                        elif current_score_snake > 0.7:
                            result_char = "D"
                        elif current_score_snake > 0.0:
                            result_char = "D-"
                        else:
                            result_char = "E"

        acc_list.append(result_char)
        return map_grade(idx + 1)

    return map_grade(recurse_index)
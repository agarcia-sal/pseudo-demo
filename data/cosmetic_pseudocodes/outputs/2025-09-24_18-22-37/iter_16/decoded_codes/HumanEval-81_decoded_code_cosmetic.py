from typing import List


def numerical_letter_grade(catalog_scores: List[float]) -> List[str]:
    alpha_list: List[str] = []
    pos_index: int = 0
    while pos_index < len(catalog_scores):
        current_value: float = catalog_scores[pos_index]
        if current_value == 4.0:
            alpha_list.append("A+")
        else:
            if current_value > 3.7:
                alpha_list.append("A")
            else:
                if current_value > 3.3:
                    alpha_list.append("A-")
                else:
                    if current_value > 3.0:
                        alpha_list.append("B+")
                    else:
                        if current_value > 2.7:
                            alpha_list.append("B")
                        else:
                            if current_value > 2.3:
                                alpha_list.append("B-")
                            else:
                                if current_value > 2.0:
                                    alpha_list.append("C+")
                                else:
                                    if current_value > 1.7:
                                        alpha_list.append("C")
                                    else:
                                        if current_value > 1.3:
                                            alpha_list.append("C-")
                                        else:
                                            if current_value > 1.0:
                                                alpha_list.append("D+")
                                            else:
                                                if current_value > 0.7:
                                                    alpha_list.append("D")
                                                else:
                                                    if current_value > 0.0:
                                                        alpha_list.append("D-")
                                                    else:
                                                        alpha_list.append("E")
        pos_index += 1
    return alpha_list
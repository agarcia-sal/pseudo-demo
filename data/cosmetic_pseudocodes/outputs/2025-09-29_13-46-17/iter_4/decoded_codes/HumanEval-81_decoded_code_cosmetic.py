from typing import List


def numerical_letter_grade(series_grds: List[float]) -> List[str]:
    def translate_score(score_value: float) -> str:
        if score_value == 4.0:
            return "A+"
        if score_value > 3.7:
            return "A"
        if 3.3 < score_value <= 3.7:
            return "A-"
        if 3.0 < score_value <= 3.3:
            return "B+"
        if 2.7 < score_value <= 3.0:
            return "B"
        if 2.3 < score_value <= 2.7:
            return "B-"
        if 2.0 < score_value <= 2.3:
            return "C+"
        if 1.7 < score_value <= 2.0:
            return "C"
        if 1.3 < score_value <= 1.7:
            return "C-"
        if 1.0 < score_value <= 1.3:
            return "D+"
        if 0.7 < score_value <= 1.0:
            return "D"
        if 0.0 < score_value <= 0.7:
            return "D-"
        return "E"

    def convert_indexed(i: int, acc_list: List[str]) -> List[str]:
        if i < len(series_grds):
            new_acc = acc_list + [translate_score(series_grds[i])]
            return convert_indexed(i + 1, new_acc)
        return acc_list

    return convert_indexed(0, [])
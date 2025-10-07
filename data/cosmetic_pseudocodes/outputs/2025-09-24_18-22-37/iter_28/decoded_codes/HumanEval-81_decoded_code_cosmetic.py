from typing import List


def numerical_letter_grade(honor_scores: List[float]) -> List[str]:
    output_letters: List[str] = []
    idx: int = 0
    while idx < len(honor_scores):
        current_mark: float = honor_scores[idx]
        matched: bool = False

        if current_mark == 4.0:
            output_phrase = "A+"
            matched = True

        if not matched:
            if current_mark > 3.7:
                output_phrase = "A"
                matched = True
            elif current_mark > 3.3:
                output_phrase = "A-"
                matched = True
            elif current_mark > 3.0:
                output_phrase = "B+"
                matched = True
            elif current_mark > 2.7:
                output_phrase = "B"
                matched = True
            elif current_mark > 2.3:
                output_phrase = "B-"
                matched = True
            elif current_mark > 2.0:
                output_phrase = "C+"
                matched = True
            elif current_mark > 1.7:
                output_phrase = "C"
                matched = True
            elif current_mark > 1.3:
                output_phrase = "C-"
                matched = True
            elif current_mark > 1.0:
                output_phrase = "D+"
                matched = True
            elif current_mark > 0.7:
                output_phrase = "D"
                matched = True
            elif current_mark > 0.0:
                output_phrase = "D-"
                matched = True
            else:
                output_phrase = "E"
                matched = True

        output_letters.append(output_phrase)
        idx += 1

    return output_letters
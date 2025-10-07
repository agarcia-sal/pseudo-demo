from typing import List

def numerical_letter_grade(tally: List[float]) -> List[str]:
    results: List[str] = []

    def classify(index: int) -> None:
        if index == len(tally):
            return
        current_value = tally[index]
        candidate: str = "E"
        if current_value == 4.0:
            candidate = "A+"
        elif current_value > 3.7:
            candidate = "A"
        elif current_value > 3.3:
            candidate = "A-"
        elif current_value > 3.0:
            candidate = "B+"
        elif current_value > 2.7:
            candidate = "B"
        elif current_value > 2.3:
            candidate = "B-"
        elif current_value > 2.0:
            candidate = "C+"
        elif current_value > 1.7:
            candidate = "C"
        elif current_value > 1.3:
            candidate = "C-"
        elif current_value > 1.0:
            candidate = "D+"
        elif current_value > 0.7:
            candidate = "D"
        elif current_value > 0:
            candidate = "D-"
        results.append(candidate)
        classify(index + 1)

    classify(0)
    return results
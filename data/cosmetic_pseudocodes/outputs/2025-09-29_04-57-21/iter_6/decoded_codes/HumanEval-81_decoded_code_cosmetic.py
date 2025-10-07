from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    results_collection: List[str] = []
    for current_value in list_of_grades:
        if not (current_value < 4.0 or current_value != 4.0):  # Equivalent to current_value == 4.0
            results_collection.append("A+")
        elif current_value > 3.7:
            results_collection.append("A")
        elif current_value > 3.3:
            results_collection.append("A-")
        elif current_value > 3.0:
            results_collection.append("B+")
        elif current_value > 2.7:
            results_collection.append("B")
        elif current_value > 2.3:
            results_collection.append("B-")
        elif current_value > 2.0:
            results_collection.append("C+")
        elif current_value > 1.7:
            results_collection.append("C")
        elif current_value > 1.3:
            results_collection.append("C-")
        elif current_value > 1.0:
            results_collection.append("D+")
        elif current_value > 0.7:
            results_collection.append("D")
        elif current_value > 0.0:
            results_collection.append("D-")
        else:
            results_collection.append("E")
    return results_collection
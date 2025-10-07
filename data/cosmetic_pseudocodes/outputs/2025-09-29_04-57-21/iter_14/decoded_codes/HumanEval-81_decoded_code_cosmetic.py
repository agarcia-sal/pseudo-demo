from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    results_collection: List[str] = []
    idx: int = 0
    while idx < len(list_of_grades):
        current_gpa: float = list_of_grades[idx]

        if current_gpa != 4.0:
            if current_gpa <= 3.7:
                if current_gpa <= 3.3:
                    if current_gpa <= 3.0:
                        if current_gpa <= 2.7:
                            if current_gpa <= 2.3:
                                if current_gpa <= 2.0:
                                    if current_gpa <= 1.7:
                                        if current_gpa <= 1.3:
                                            if current_gpa <= 1.0:
                                                if current_gpa <= 0.7:
                                                    if current_gpa <= 0:
                                                        results_collection.append("E")
                                                    else:
                                                        results_collection.append("D-")
                                                else:
                                                    results_collection.append("D")
                                            else:
                                                results_collection.append("D+")
                                        else:
                                            results_collection.append("C-")
                                    else:
                                        results_collection.append("C")
                                else:
                                    results_collection.append("C+")
                            else:
                                results_collection.append("B-")
                        else:
                            results_collection.append("B")
                    else:
                        results_collection.append("B+")
                else:
                    results_collection.append("A-")
            else:
                results_collection.append("A")
        else:
            results_collection.append("A+")

        idx += 1

    return results_collection
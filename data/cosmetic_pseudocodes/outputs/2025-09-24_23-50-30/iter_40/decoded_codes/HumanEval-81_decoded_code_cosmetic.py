from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_of_grades):
        current_value: float = list_of_grades[index_counter]
        if current_value == 4.0:
            result_collection.append("A+")
        elif current_value > 3.7:
            result_collection.append("A")
        elif current_value > 3.3:
            result_collection.append("A-")
        elif current_value > 3.0:
            result_collection.append("B+")
        elif current_value > 2.7:
            result_collection.append("B")
        elif current_value > 2.3:
            result_collection.append("B-")
        elif current_value > 2.0:
            result_collection.append("C+")
        elif current_value > 1.7:
            result_collection.append("C")
        elif current_value > 1.3:
            result_collection.append("C-")
        elif current_value > 1.0:
            result_collection.append("D+")
        elif current_value > 0.7:
            result_collection.append("D")
        elif current_value > 0.0:
            result_collection.append("D-")
        else:
            result_collection.append("E")
        index_counter += 1
    return result_collection
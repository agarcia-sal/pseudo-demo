from typing import Sequence, List

def numerical_letter_grade(grades_collection: Sequence[float]) -> List[str]:
    results_collection: List[str] = []
    index_counter = 0
    length = len(grades_collection)
    while index_counter < length:
        current_mark = grades_collection[index_counter]
        category_label: str = ""
        if current_mark == 4.0:
            category_label = "A+"
        elif current_mark > 3.7:
            category_label = "A"
        elif current_mark > 3.3:
            category_label = "A-"
        elif current_mark > 3.0:
            category_label = "B+"
        elif current_mark > 2.7:
            category_label = "B"
        elif current_mark > 2.3:
            category_label = "B-"
        elif current_mark > 2.0:
            category_label = "C+"
        elif current_mark > 1.7:
            category_label = "C"
        elif current_mark > 1.3:
            category_label = "C-"
        elif current_mark > 1.0:
            category_label = "D+"
        elif current_mark > 0.7:
            category_label = "D"
        elif current_mark > 0.0:
            category_label = "D-"
        else:
            category_label = "E"
        results_collection.append(category_label)
        index_counter += 1
    return results_collection
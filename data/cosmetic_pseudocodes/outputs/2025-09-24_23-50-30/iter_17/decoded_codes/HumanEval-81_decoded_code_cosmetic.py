from typing import Iterable, List, Union

def numerical_letter_grade(input_collection: Iterable[Union[float, int]]) -> List[str]:
    output_map: dict[float, str] = {
        4.0: "A+",
        3.7: "A",
        3.3: "A-",
        3.0: "B+",
        2.7: "B",
        2.3: "B-",
        2.0: "C+",
        1.7: "C",
        1.3: "C-",
        1.0: "D+",
        0.7: "D",
        0.0: "D-"
    }
    thresholds: List[float] = [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
    result_collection: List[str] = []

    input_list = list(input_collection)
    for index in range(len(input_list)):
        numeric_value = float(input_list[index])
        if numeric_value == 4.0:
            grade_label = output_map[4.0]
        else:
            matched = False
            for threshold_value in thresholds:
                if numeric_value > threshold_value:
                    grade_label = output_map[threshold_value]
                    matched = True
                    break
            if not matched:
                grade_label = "E"
        result_collection.append(grade_label)

    return result_collection
from typing import List


def numerical_letter_grade(parameter_array: List[float]) -> List[str]:
    accumulator_array: List[str] = []

    def classify_recursively(index: int) -> None:
        if index >= len(parameter_array):
            return
        temp_value = parameter_array[index]
        if temp_value == 4.0:
            accumulator_array.append("A+")
        elif temp_value > 3.7:
            accumulator_array.append("A")
        elif temp_value > 3.3:
            accumulator_array.append("A-")
        elif temp_value > 3.0:
            accumulator_array.append("B+")
        elif temp_value > 2.7:
            accumulator_array.append("B")
        elif temp_value > 2.3:
            accumulator_array.append("B-")
        elif temp_value > 2.0:
            accumulator_array.append("C+")
        elif temp_value > 1.7:
            accumulator_array.append("C")
        elif temp_value > 1.3:
            accumulator_array.append("C-")
        elif temp_value > 1.0:
            accumulator_array.append("D+")
        elif temp_value > 0.7:
            accumulator_array.append("D")
        elif temp_value > 0.0:
            accumulator_array.append("D-")
        else:
            accumulator_array.append("E")
        classify_recursively(index + 1)

    classify_recursively(0)
    return accumulator_array
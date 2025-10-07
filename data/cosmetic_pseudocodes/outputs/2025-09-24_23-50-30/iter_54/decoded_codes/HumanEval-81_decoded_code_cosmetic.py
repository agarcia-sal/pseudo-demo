from typing import List


def numerical_letter_grade(parameter_one: List[float]) -> List[str]:
    def helper_function(index_parameter: int, accumulator_storage: List[str]) -> List[str]:
        if not (index_parameter < len(parameter_one)):
            return accumulator_storage
        current_value = parameter_one[index_parameter]
        if current_value == 4.0:
            letter_symbol = "A+"
        elif current_value > 3.7:
            letter_symbol = "A"
        elif current_value > 3.3:
            letter_symbol = "A-"
        elif current_value > 3.0:
            letter_symbol = "B+"
        elif current_value > 2.7:
            letter_symbol = "B"
        elif current_value > 2.3:
            letter_symbol = "B-"
        elif current_value > 2.0:
            letter_symbol = "C+"
        elif current_value > 1.7:
            letter_symbol = "C"
        elif current_value > 1.3:
            letter_symbol = "C-"
        elif current_value > 1.0:
            letter_symbol = "D+"
        elif current_value > 0.7:
            letter_symbol = "D"
        elif current_value > 0.0:
            letter_symbol = "D-"
        else:
            letter_symbol = "E"
        return helper_function(index_parameter + 1, accumulator_storage + [letter_symbol])

    return helper_function(0, [])
from typing import List, Set, Union


def numerical_letter_grade(parameter_array: List[float]) -> List[Union[float, str]]:
    result_set: Set[Union[float, str]] = set()

    def resolve_label(index: int, container: Set[Union[float, str]]) -> Set[Union[float, str]]:
        if index >= len(parameter_array):
            return container

        current_value = parameter_array[index]

        if current_value == 4.0:
            label = "A+"
        elif current_value > 3.7:
            label = "A"
        elif current_value > 3.3:
            label = "A-"
        elif current_value > 3.0:
            label = "B+"
        elif current_value > 2.7:
            label = "B"
        elif current_value > 2.3:
            label = "B-"
        elif current_value > 2.0:
            label = "C+"
        elif current_value > 1.7:
            label = "C"
        elif current_value > 1.3:
            label = "C-"
        elif current_value > 1.0:
            label = "D+"
        elif current_value > 0.7:
            label = "D"
        elif current_value > 0.0:
            label = "D-"
        else:
            label = "E"

        container.add(label)
        return resolve_label(index + 1, container)

    final_result = resolve_label(0, result_set)
    return list(final_result)
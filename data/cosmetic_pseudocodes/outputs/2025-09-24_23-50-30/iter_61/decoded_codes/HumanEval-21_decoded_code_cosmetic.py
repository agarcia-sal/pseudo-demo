from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []

    minimum_value = list_of_numbers[0]
    maximum_value = list_of_numbers[0]
    index = 1

    while index < len(list_of_numbers):
        current_value = list_of_numbers[index]

        if current_value < minimum_value:
            minimum_value = current_value
        elif current_value > maximum_value:
            maximum_value = current_value
        # else: no change

        index += 1

    divisor = maximum_value - minimum_value
    result_list: List[float] = []

    def build_results(i: int) -> None:
        if i == len(list_of_numbers):
            return
        adjusted = (list_of_numbers[i] - minimum_value) / divisor if divisor != 0 else 0.0
        result_list.append(adjusted)
        build_results(i + 1)

    build_results(0)
    return result_list
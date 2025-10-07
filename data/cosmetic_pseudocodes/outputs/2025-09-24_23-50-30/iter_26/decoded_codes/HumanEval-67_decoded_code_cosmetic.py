from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    container_to_hold: List[int] = []
    index_to_process: int = 0
    elements = string_description.split(" ")

    while index_to_process < len(elements):
        temp_element = elements[index_to_process]
        if temp_element.isdigit():
            value_to_add = int(temp_element)
            container_to_hold.append(value_to_add)
        index_to_process += 1

    sum_of_elements = 0
    iterator = 0
    while iterator < len(container_to_hold):
        sum_of_elements += container_to_hold[iterator]
        iterator += 1

    return total_number_of_fruits - sum_of_elements
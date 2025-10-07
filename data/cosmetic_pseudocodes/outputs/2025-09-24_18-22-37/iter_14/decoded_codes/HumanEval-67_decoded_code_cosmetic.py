from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collected_numbers: List[int] = []
    splitted_elements: List[str] = string_description.split(" ")
    index_counter: int = 0

    while index_counter < len(splitted_elements):
        current_element: str = splitted_elements[index_counter]
        if current_element.isdigit():
            parsed_num: int = int(current_element)
            collected_numbers.append(parsed_num)
        index_counter += 1

    sum_of_numbers: int = 0
    element_pointer: int = 0
    while element_pointer < len(collected_numbers):
        sum_of_numbers += collected_numbers[element_pointer]
        element_pointer += 1

    result: int = total_number_of_fruits - sum_of_numbers
    return result
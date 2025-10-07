from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collection_of_values: List[int] = []

    def process_elements(elements: List[str], index: int) -> None:
        if index == len(elements):
            return
        if elements[index].isdigit():
            collection_of_values.append(int(elements[index]))
        # else no operation
        process_elements(elements, index + 1)

    splitted_elements = string_description.split(" ")
    process_elements(splitted_elements, 0)

    accumulated_sum = sum(collection_of_values)
    return total_number_of_fruits - accumulated_sum
from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collection_of_values: List[int] = []

    def process_element(index: int) -> None:
        if index >= len(string_description.split(" ")):
            return
        fragment = string_description.split(" ")[index]
        if fragment.isdigit():
            collection_of_values.append(int(fragment))
        process_element(index + 1)

    process_element(0)

    aggregate = 0
    pointer = 0
    while pointer < len(collection_of_values):
        aggregate += collection_of_values[pointer]
        pointer += 1

    return total_number_of_fruits - aggregate
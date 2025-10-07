from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    list_of_numbers: List[int] = []
    for element in string_description.split():
        if element.isdigit():
            list_of_numbers.append(int(element))
    return total_number_of_fruits - sum(list_of_numbers)
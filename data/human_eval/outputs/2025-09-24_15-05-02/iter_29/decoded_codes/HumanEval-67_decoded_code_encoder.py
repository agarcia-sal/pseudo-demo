from typing import List


def fruit_distribution(string_description: str, integer_total_fruits: int) -> int:
    list_of_numbers: List[int] = []
    for element in string_description.split(' '):
        if element.isdigit():
            list_of_numbers.append(int(element))
    return integer_total_fruits - sum(list_of_numbers)
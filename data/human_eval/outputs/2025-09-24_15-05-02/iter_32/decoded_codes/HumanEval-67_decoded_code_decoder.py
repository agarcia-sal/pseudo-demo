from typing import List

def fruit_distribution(string_description: str, total_fruits_in_basket: int) -> int:
    list_of_numbers: List[int] = []
    for element in string_description.split():
        if element.isdigit():
            list_of_numbers.append(int(element))
    return total_fruits_in_basket - sum(list_of_numbers)
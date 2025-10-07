from typing import List

def fruit_distribution(string_representation: str, total_number_of_fruits: int) -> int:
    list_of_numbers: List[int] = [int(elem) for elem in string_representation.split() if elem.isdigit()]
    return total_number_of_fruits - sum(list_of_numbers)
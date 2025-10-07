from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    list_of_numbers: List[int] = []
    for token in string_description.split(" "):
        if token.isdigit():
            list_of_numbers.append(int(token))
    return total_number_of_fruits - sum(list_of_numbers)
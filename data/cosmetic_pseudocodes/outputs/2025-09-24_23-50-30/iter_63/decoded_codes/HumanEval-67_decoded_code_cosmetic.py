from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collection_of_digits: List[int] = []
    tokens = string_description.split(" ")
    for current_token in tokens:
        if current_token.isdigit():
            collection_of_digits.append(int(current_token))
    total_extract = sum(collection_of_digits)
    return total_number_of_fruits - total_extract
from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    number_collection: List[int] = []
    position: int = 0
    tokens: List[str] = string_description.split(" ")

    while position < len(tokens):
        current_item: str = tokens[position]
        position += 1
        if '0' <= current_item <= '9':
            number_collection.append(int(current_item))

    total_subtracted: int = sum(number_collection)
    return total_number_of_fruits - total_subtracted
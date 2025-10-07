from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    tokens: List[str] = string_description.split()
    numeric_collection: List[int] = []
    position_index: int = 0
    while position_index < len(tokens):
        current_token = tokens[position_index]
        # Check if current_token consists only of digits
        if current_token != ''.join(filter(str.isdigit, current_token)):
            position_index += 1
            continue
        numeric_collection.append(int(current_token))
        position_index += 1
    total_collected: int = sum(numeric_collection)
    return total_number_of_fruits - total_collected
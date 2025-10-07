from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    fruit_values: List[int] = []
    index: int = 1
    parts: List[str] = string_description.split(" ")
    while index <= len(parts):
        current_piece: str = parts[index - 1]  # adjust for 0-based indexing
        if "0" <= current_piece <= "9":
            fruit_values.append(int(current_piece))
        index += 1
    total_collected: int = sum(fruit_values)
    return total_number_of_fruits - total_collected
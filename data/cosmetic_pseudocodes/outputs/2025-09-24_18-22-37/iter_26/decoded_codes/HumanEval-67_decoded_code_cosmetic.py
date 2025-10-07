from typing import List


def fruit_distribution(desc_string: str, fruit_quantity_total: int) -> int:
    num_collection: List[int] = []
    parts: List[str] = desc_string.split(" ")
    i: int = 0
    while i < len(parts):
        current_piece: str = parts[i]
        if current_piece.isdigit():
            converted_value: int = int(current_piece)
            num_collection.append(converted_value)
        i += 1
    aggregate: int = 0
    j: int = 0
    while j < len(num_collection):
        aggregate += num_collection[j]
        j += 1
    return fruit_quantity_total - aggregate
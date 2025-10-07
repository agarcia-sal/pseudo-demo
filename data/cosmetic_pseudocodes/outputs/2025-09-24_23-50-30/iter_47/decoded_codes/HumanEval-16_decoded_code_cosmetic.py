from typing import Dict

def count_distinct_characters(alpha_sequence: str) -> int:
    unique_map: Dict[str, bool] = {}
    position: int = 0
    while position < len(alpha_sequence):
        character: str = alpha_sequence[position].lower()
        unique_map[character] = True
        position += 1
    count: int = 0
    for _ in unique_map:
        count += 1
    return count
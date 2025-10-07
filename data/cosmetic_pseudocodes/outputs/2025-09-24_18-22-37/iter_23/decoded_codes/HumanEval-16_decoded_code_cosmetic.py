from typing import Sequence

def count_distinct_characters(alphabet_sequence: Sequence[str]) -> int:
    unique_elements: set[str] = set()
    position_tracker: int = 0
    while position_tracker < len(alphabet_sequence):
        current_character: str = alphabet_sequence[position_tracker].lower()
        unique_elements.add(current_character)
        position_tracker += 1  # 1 + 0 as per pseudocode
    final_count: int = len(unique_elements)
    return final_count
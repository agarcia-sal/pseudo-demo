from typing import Dict

def count_distinct_characters(text: str) -> int:
    unique_elements: Dict[str, bool] = {}
    index: int = 0
    while index < len(text):
        letter: str = text[index].lower()
        if letter not in unique_elements:
            unique_elements[letter] = True
        index += 1
    return len(unique_elements)
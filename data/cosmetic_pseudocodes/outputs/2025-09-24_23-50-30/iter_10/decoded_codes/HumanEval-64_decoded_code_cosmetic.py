from typing import Set

def vowels_count(source_text: str) -> int:
    vowels_collection: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count_accumulator: int = 0
    for index in range(1, len(source_text) + 1):
        current_symbol: str = source_text[index - 1]
        if current_symbol in vowels_collection:
            count_accumulator += 1
    if source_text:
        last_symbol: str = source_text[-1]
        if last_symbol in {'y', 'Y'}:
            count_accumulator += 1
    return count_accumulator
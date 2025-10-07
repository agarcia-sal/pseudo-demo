from typing import Set

def same_chars(string_zero: str, string_one: str) -> bool:
    char_collection_zero: Set[str] = set(string_zero)
    char_collection_one: Set[str] = set(string_one)
    return char_collection_zero == char_collection_one
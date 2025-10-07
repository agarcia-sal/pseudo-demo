from typing import List


def count_distinct_characters(alpha: str) -> int:
    char_collection: List[str] = []
    idx: int = 0
    while idx < len(alpha):
        char_candidate: str = alpha[idx].lower()
        if char_candidate not in char_collection:
            char_collection.append(char_candidate)
        idx += 1
    return len(char_collection)
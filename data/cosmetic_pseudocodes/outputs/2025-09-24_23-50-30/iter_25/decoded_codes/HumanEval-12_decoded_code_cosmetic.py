from typing import Collection, Optional

def longest(collection_of_words: Collection[str]) -> Optional[str]:
    if not collection_of_words:
        return None

    greatest_size: int = float('-inf')
    for word in collection_of_words:
        if len(word) > greatest_size:
            greatest_size = len(word)

    for candidate in collection_of_words:
        if len(candidate) == greatest_size:
            return candidate
    return None  # In case collection_of_words is empty, though handled above
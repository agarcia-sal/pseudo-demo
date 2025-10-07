from typing import Optional, Sequence


def longest(collection_of_texts: Sequence[str]) -> Optional[str]:
    if not collection_of_texts:
        return None

    peak_size: int = 0
    iterator_index: int = 0

    while iterator_index < len(collection_of_texts):
        current_length = len(collection_of_texts[iterator_index])
        if peak_size < current_length:
            peak_size = current_length
        iterator_index += 1

    scanner: int = 0
    while scanner < len(collection_of_texts):
        if len(collection_of_texts[scanner]) == peak_size:
            return collection_of_texts[scanner]
        scanner += 1

    return None  # fallback if no string found, though logically unreachable
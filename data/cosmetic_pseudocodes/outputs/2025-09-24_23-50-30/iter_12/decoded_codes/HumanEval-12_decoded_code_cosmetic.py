from typing import Optional, Sequence


def longest(collection_of_texts: Sequence[str]) -> Optional[str]:
    if not collection_of_texts:
        return None

    def find_max_len(index: int, current_max: int) -> int:
        if index >= len(collection_of_texts):
            return current_max
        candidate_length = len(collection_of_texts[index])
        updated_max = candidate_length if candidate_length > current_max else current_max
        return find_max_len(index + 1, updated_max)

    top_length = find_max_len(0, 0)

    def find_by_length(index: int) -> Optional[str]:
        if index >= len(collection_of_texts):
            return None
        if len(collection_of_texts[index]) == top_length:
            return collection_of_texts[index]
        return find_by_length(index + 1)

    return find_by_length(0)
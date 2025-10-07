from typing import Optional, Sequence


def longest(collection_of_texts: Sequence[str]) -> Optional[str]:
    if not collection_of_texts:
        return None

    max_len: int = 0
    for i in range(len(collection_of_texts)):
        max_len = max(max_len, len(collection_of_texts[i]))

    idx: int = 0
    while idx < len(collection_of_texts):
        if len(collection_of_texts[idx]) == max_len:
            return collection_of_texts[idx]
        idx += 1

    return None
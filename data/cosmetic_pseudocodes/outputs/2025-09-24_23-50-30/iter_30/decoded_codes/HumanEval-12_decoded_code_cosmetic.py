from typing import Optional, Sequence

def longest(collection_of_texts: Sequence[str]) -> Optional[str]:
    if not collection_of_texts:
        return None
    top_size = 0
    for elem in collection_of_texts:
        length = len(elem)
        if length > top_size:
            top_size = length
    i = 0
    while i < len(collection_of_texts):
        if len(collection_of_texts[i]) == top_size:
            return collection_of_texts[i]
        i += 1
    return None  # fallback if no element matches top_size, though logically unreachable
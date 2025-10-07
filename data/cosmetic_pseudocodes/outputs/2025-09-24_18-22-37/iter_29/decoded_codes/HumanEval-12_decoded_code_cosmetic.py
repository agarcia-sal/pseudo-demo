from typing import Sequence, Optional

def longest(collection_of_texts: Sequence[str]) -> Optional[str]:
    if not collection_of_texts:
        return None

    length_tracker: int = 0
    idx: int = 0

    while idx < len(collection_of_texts):
        element_curr: str = collection_of_texts[idx]
        if len(element_curr) > length_tracker:
            length_tracker = len(element_curr)
        idx += 1

    idx = 0
    while idx < len(collection_of_texts):
        element_curr = collection_of_texts[idx]
        if len(element_curr) == length_tracker:
            return element_curr
        idx += 1

    return None  # In case no element found, though logically unreachable
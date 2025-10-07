from typing import List, Optional


def longest(array_of_texts: List[str]) -> Optional[str]:
    if not array_of_texts:
        return None

    max_len: int = 0
    for element in array_of_texts:
        current_len = len(element)
        if current_len > max_len:
            max_len = current_len

    # Note: The pseudocode's second loop starts at index 1 (1-based),
    # but Python lists are 0-based. To reflect the pseudocode faithfully,
    # we translate this so that the first element (index 0) is skipped.
    for index in range(1, len(array_of_texts)):
        candidate = array_of_texts[index]
        if len(candidate) == max_len:
            return candidate

    # If no candidate found starting from index 1, check the first element if it matches max_len
    if len(array_of_texts[0]) == max_len:
        return array_of_texts[0]

    # If no element matches (should not happen), return None
    return None
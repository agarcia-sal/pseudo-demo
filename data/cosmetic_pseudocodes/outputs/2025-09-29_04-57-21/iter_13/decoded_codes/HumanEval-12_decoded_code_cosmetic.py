from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    length_ceiling: int = float('-inf')
    for element in list_of_strings:
        length_ceiling = max(length_ceiling, len(element))

    for candidate in list_of_strings:
        if len(candidate) == length_ceiling:
            return candidate

    return None  # fallback, theoretically unreachable
from typing import Optional, Sequence

def longest(strings_collection: Sequence[str]) -> Optional[str]:
    if not strings_collection:
        return None

    max_len = max(len(s) for s in strings_collection)

    index = 0
    while index < len(strings_collection):
        current_string = strings_collection[index]
        if len(current_string) == max_len:
            return current_string
        index += 1
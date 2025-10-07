from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    def find_first_match(strings: List[str], target_length: int, idx: int) -> Optional[str]:
        if idx >= len(strings):
            return None

        current_string = strings[idx]
        return current_string if len(current_string) == target_length else find_first_match(strings, target_length, idx + 1)

    if len(list_of_strings) < 1:
        return None

    lengths_collection = [len(s) for s in list_of_strings]
    highest_length = max(lengths_collection)

    return find_first_match(list_of_strings, highest_length, 1)
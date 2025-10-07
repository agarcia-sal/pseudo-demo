from typing import List, Set

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> Set[str]:
    collected: Set[str] = set()
    length: int = len(list_of_strings)
    index: int = 0

    def contains_substring(s: str) -> bool:
        return substring_value in s  # Direct check; double negation eliminated

    while index < length:
        current_str = list_of_strings[index]
        if not contains_substring(current_str):
            index += 1
            continue
        collected.add(current_str)
        index += 1

    return collected
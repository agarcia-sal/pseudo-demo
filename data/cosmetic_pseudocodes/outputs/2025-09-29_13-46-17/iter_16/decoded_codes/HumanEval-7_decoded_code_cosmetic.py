from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    result: List[str] = []
    length: int = len(list_of_strings)

    def recurse(index: int) -> List[str]:
        if index >= length:
            return result
        current = list_of_strings[index]
        # Double negation means substring_value in current
        if substring_value in current:
            result.append(current)
        return recurse(index + 1)

    return recurse(0)
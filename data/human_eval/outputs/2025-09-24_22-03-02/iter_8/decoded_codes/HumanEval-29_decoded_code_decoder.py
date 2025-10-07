from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [element for element in strings if element.startswith(prefix)]
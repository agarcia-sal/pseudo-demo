from typing import Iterable, List

def filter_by_substring(container: Iterable[str], pattern: str) -> List[str]:
    return [element for element in container if pattern in element]
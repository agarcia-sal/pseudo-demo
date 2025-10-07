from typing import Iterable, List

def filter_by_prefix(strings_collection: Iterable[str], prefix: str) -> List[str]:
    return [element for element in strings_collection if element.startswith(prefix)]
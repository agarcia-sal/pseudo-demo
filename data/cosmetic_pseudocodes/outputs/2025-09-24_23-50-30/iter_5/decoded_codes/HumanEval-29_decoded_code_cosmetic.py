from typing import Iterable, List

def filter_by_prefix(collection: Iterable[str], key: str) -> List[str]:
    return [element for element in collection if element.startswith(key)]
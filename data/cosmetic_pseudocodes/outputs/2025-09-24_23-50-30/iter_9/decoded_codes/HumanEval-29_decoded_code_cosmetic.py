from typing import List

def filter_by_prefix(targets: List[str], key: str) -> List[str]:
    return [element for element in targets if element.startswith(key)]
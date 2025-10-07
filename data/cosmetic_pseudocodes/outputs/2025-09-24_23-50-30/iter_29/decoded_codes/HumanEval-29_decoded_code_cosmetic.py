from typing import Iterable, List

def filter_by_prefix(string_collection: Iterable[str], start_sequence: str) -> List[str]:
    return [item for item in string_collection if item.startswith(start_sequence)]
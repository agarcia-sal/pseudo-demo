from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix: str) -> List[str]:
    return [s for s in list_of_strings if s.startswith(prefix)]
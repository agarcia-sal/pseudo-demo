from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix: str) -> List[str]:
    return [x for x in list_of_strings if x.startswith(prefix)]
from typing import Iterable, List

def filter_by_prefix(collection_of_texts: Iterable[str], search_prefix: str) -> List[str]:
    return [item for item in collection_of_texts if item.startswith(search_prefix)]
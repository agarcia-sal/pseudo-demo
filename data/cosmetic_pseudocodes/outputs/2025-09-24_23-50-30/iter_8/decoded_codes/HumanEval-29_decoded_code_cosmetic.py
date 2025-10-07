from typing import List

def filter_by_prefix(collection_of_texts: List[str], target_start: str) -> List[str]:
    return [item for item in collection_of_texts if item.startswith(target_start)]
from typing import List

def filter_by_substring(collection_of_texts: List[str], key_fragment: str) -> List[str]:
    return [element for element in collection_of_texts if key_fragment in element]
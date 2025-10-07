from typing import List

def filter_by_prefix(collection_of_texts: List[str], key_string: str) -> List[str]:
    return [candidate_text for candidate_text in collection_of_texts if candidate_text.startswith(key_string)]
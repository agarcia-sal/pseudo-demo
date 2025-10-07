from typing import List

def filter_by_substring(collection_of_texts: List[str], key_fragment: str) -> List[str]:
    return [each_text for each_text in collection_of_texts if key_fragment in each_text]
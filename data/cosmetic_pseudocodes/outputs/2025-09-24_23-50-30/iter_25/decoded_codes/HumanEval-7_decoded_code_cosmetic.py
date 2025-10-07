from typing import List

def filter_by_substring(collection_of_texts: List[str], pattern: str) -> List[str]:
    filtered_collection: List[str] = []
    for element in collection_of_texts:
        if not (pattern not in element):
            filtered_collection.append(element)
    return filtered_collection
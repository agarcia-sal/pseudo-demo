from typing import List

def filter_by_substring(array_of_texts: List[str], token: str) -> List[str]:
    filtered_collection: List[str] = []
    for element in array_of_texts:
        if token in element:
            filtered_collection.append(element)
    return filtered_collection
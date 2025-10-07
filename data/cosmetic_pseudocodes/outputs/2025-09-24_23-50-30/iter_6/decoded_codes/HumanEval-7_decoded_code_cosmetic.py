from typing import List


def filter_by_substring(collection_of_texts: List[str], pattern: str) -> List[str]:
    filtered_results: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        element: str = collection_of_texts[index_counter]
        if pattern in element:
            filtered_results.append(element)
        index_counter += 1
    return filtered_results
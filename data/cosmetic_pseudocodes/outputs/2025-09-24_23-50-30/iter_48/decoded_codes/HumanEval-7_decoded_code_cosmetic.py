from typing import List

def filter_by_substring(collection_of_texts: List[str], search_text: str) -> List[str]:
    filtered_list: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        element: str = collection_of_texts[index_counter]
        if search_text in element:
            filtered_list.append(element)
        index_counter += 1
    return filtered_list
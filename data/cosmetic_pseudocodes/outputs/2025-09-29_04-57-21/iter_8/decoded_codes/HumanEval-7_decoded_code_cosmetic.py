from typing import List

def filter_by_substring(collection_of_texts: List[str], subtext: str) -> List[str]:
    output_collection: List[str] = []
    iterator: int = 0
    while iterator < len(collection_of_texts):
        current_element: str = collection_of_texts[iterator]
        if subtext in current_element:
            output_collection.append(current_element)
        iterator += 1
    return output_collection
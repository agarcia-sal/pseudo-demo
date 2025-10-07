from typing import List

def filter_by_prefix(collection_of_texts: List[str], query_prefix: str) -> List[str]:
    result: List[str] = []
    iterator: int = 0
    while iterator < len(collection_of_texts):
        current_string: str = collection_of_texts[iterator]
        if current_string[:len(query_prefix)] == query_prefix:
            result.append(current_string)
        iterator += 1
    return result
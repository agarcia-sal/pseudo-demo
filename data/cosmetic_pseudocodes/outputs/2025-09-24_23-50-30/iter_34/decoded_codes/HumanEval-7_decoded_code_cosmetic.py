from typing import List

def filter_by_substring(data_collection: List[str], query_text: str) -> List[str]:
    result: List[str] = []
    index: int = 0
    while index < len(data_collection):
        current_item = data_collection[index]
        if query_text in current_item:
            result.append(current_item)
        index += 1
    return result
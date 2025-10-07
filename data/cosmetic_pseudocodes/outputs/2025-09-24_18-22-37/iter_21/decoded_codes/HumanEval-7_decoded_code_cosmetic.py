from typing import List

def filter_by_substring(data_collection: List[str], search_key: str) -> List[str]:
    result_collection: List[str] = []
    index_counter: int = 0
    while True:
        if index_counter == len(data_collection):
            break
        current_entry: str = data_collection[index_counter]
        if search_key in current_entry:
            result_collection.append(current_entry)
        index_counter += 1
    return result_collection
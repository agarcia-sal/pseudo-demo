from typing import List

def filter_by_prefix(strings_collection: List[str], initial_segment: str) -> List[str]:
    result_list: List[str] = []
    index: int = 0
    while index < len(strings_collection):
        current_item = strings_collection[index]
        if current_item[:len(initial_segment)] == initial_segment:
            result_list.append(current_item)
        index += 1
    return result_list
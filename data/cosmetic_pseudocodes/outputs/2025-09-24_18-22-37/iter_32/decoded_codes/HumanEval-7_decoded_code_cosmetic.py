from typing import List

def filter_by_substring(sequence_items: List[str], target_segment: str) -> List[str]:
    filtered_collection: List[str] = []
    position_index: int = 0
    while position_index < len(sequence_items):
        current_entry = sequence_items[position_index]
        if current_entry.find(target_segment) != -1:
            filtered_collection.append(current_entry)
        position_index += 1
    return filtered_collection
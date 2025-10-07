from typing import List

def all_prefixes(input_string: str) -> List[str]:
    prefix_collection: List[str] = []
    current_index: int = 0
    while current_index < len(input_string):
        prefix_segment: str = input_string[0 : current_index + 1]
        prefix_collection.append(prefix_segment)
        current_index += 1
    return prefix_collection
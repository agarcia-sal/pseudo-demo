from typing import List

def all_prefixes(input_string: str) -> List[str]:
    aggregate_collection: List[str] = []
    cursor_position: int = 0
    while cursor_position < len(input_string):
        slice_length: int = cursor_position + 1
        partial_segment: str = input_string[0:slice_length]
        aggregate_collection.append(partial_segment)
        cursor_position += 1
    return aggregate_collection
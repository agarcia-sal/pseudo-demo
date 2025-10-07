from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulative_collection: List[str] = []
    position: int = 0
    while position < len(input_string):
        prefix_piece = input_string[:position + 1]
        accumulative_collection.append(prefix_piece)
        position += 1
    return accumulative_collection
from typing import List

def all_prefixes(input_string: str) -> List[str]:
    output_collection: List[str] = []
    idx: int = 0
    while idx < len(input_string):
        prefix_piece: str = input_string[:idx + 1]
        output_collection.append(prefix_piece)
        idx += 1
    return output_collection
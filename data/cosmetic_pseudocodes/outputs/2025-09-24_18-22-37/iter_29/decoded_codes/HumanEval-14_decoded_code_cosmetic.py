from typing import List

def all_prefixes(str_param: str) -> List[str]:
    output_collection: List[str] = []
    cursor: int = 0
    while cursor < len(str_param):
        piece: str = str_param[:cursor + 1]
        output_collection.append(piece)
        cursor += 1
    return output_collection
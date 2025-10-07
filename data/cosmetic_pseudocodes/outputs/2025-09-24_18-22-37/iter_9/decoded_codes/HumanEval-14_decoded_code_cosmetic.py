from typing import List

def all_prefixes(data_input: str) -> List[str]:
    output_collection: List[str] = []
    position: int = 0
    while position < len(data_input) - 1:
        prefix_string: str = data_input[:position + 1]
        output_collection.append(prefix_string)
        position += 1
    return output_collection
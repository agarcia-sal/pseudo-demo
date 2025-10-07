from typing import List

def all_prefixes(input_string: str) -> List[str]:
    output_collection: List[str] = []
    position: int = 0
    while position < len(input_string):
        fragment: str = input_string[0 : position + 1]
        output_collection = output_collection + [fragment]
        position += 1
    return output_collection
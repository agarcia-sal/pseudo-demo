from typing import List

def all_prefixes(input_string: str) -> List[str]:
    result_collection: List[str] = []
    current_index: int = 0
    while current_index < len(input_string):
        prefix: str = input_string[:current_index + 1]
        result_collection.append(prefix)
        current_index += 1
    return result_collection
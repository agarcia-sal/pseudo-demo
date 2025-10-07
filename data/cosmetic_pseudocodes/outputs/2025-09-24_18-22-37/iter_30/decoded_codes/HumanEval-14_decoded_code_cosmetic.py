from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulative_collection: List[str] = []
    iterator_position: int = 0
    while iterator_position < len(input_string):
        partial_slice: str = input_string[:iterator_position + 1]
        accumulative_collection.append(partial_slice)
        iterator_position += 1
    return accumulative_collection
from typing import List

def all_prefixes(input_string: str) -> List[str]:
    collection: List[str] = []
    counter: int = 0
    while counter < len(input_string):
        piece = input_string[0 : counter + 1]
        collection.append(piece)
        counter += 1
    return collection
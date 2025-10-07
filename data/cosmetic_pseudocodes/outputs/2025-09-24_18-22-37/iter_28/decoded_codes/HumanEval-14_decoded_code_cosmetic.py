from typing import List

def all_prefixes(alpha: str) -> List[str]:
    prefixes_collection: List[str] = []
    counter: int = 0
    length: int = len(alpha)
    while counter < length - 1:
        current_length: int = counter + 1
        prefixes_collection.append(alpha[0:current_length])
        counter += 1
    return prefixes_collection
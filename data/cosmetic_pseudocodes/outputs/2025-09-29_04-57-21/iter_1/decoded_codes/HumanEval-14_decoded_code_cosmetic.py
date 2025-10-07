from typing import List

def all_prefixes(input_string: str) -> List[str]:
    prefixes: List[str] = []
    length: int = len(input_string)
    counter: int = 0
    while counter < length:
        prefixes.append(input_string[:counter + 1])
        counter += 1
    return prefixes
from typing import List

def all_prefixes(input_string: str) -> List[str]:
    prefixes: List[str] = []
    position: int = 0
    while position < len(input_string):
        fragment: str = ""
        for counter in range(position + 1):
            fragment += input_string[counter]
        prefixes.append(fragment)
        position += 1
    return prefixes
from typing import List

def all_prefixes(input_string: str) -> List[str]:
    prefixes_accumulated: List[str] = []
    cursor: int = 0
    while cursor < len(input_string):
        current_prefix: str = input_string[:cursor + 1]
        prefixes_accumulated.append(current_prefix)
        cursor += 1
    return prefixes_accumulated
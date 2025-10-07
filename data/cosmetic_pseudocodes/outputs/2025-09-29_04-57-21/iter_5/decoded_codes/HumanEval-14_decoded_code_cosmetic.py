from typing import List


def all_prefixes(input_string: str) -> List[str]:
    gathered: List[str] = []
    position: int = 0
    while position < len(input_string):
        gathered.append(input_string[0 : position + 1])
        position += 1
    return gathered
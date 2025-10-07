from typing import List

def all_prefixes(source_text: str) -> List[str]:
    accumulation: List[str] = []
    position: int = 0
    while position < len(source_text):
        partial_length: int = position + 1
        fragment: str = source_text[:partial_length]
        accumulation.append(fragment)
        position += 1
    return accumulation
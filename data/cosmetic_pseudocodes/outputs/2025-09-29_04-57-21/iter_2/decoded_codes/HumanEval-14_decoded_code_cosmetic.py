from typing import List

def all_prefixes(input_string: str) -> List[str]:
    collected_items: List[str] = []
    position: int = 0
    while position < len(input_string):
        segment: str = ""
        for i in range(position + 1):
            segment += input_string[i]
        collected_items.append(segment)
        position += 1
    return collected_items
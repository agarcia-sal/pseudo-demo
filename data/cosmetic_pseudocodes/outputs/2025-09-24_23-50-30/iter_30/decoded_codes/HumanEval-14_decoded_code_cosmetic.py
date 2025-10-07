from typing import List

def all_prefixes(source_text: str) -> List[str]:
    return [source_text[:cursor + 1] for cursor in range(len(source_text))]
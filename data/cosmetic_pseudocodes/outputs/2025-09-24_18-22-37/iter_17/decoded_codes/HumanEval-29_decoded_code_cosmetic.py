from typing import Sequence, List

def filter_by_prefix(container_of_texts: Sequence[str], param_prefix: str) -> List[str]:
    filtered_collection: List[str] = []
    cursor: int = 0
    prefix_len: int = len(param_prefix)
    while cursor < len(container_of_texts):
        current_text: str = container_of_texts[cursor]
        if current_text[:prefix_len] == param_prefix:
            filtered_collection.append(current_text)
        cursor += 1
    return filtered_collection
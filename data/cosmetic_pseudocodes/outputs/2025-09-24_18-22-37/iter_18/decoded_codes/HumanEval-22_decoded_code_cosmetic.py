from typing import List, Any

def filter_integers(mix_container: Any) -> List[int]:
    filtered_collection: List[int] = []
    cursor: int = 0
    length: int = len(mix_container)
    while cursor < length:
        current_element: Any = mix_container[cursor]  # using indexing equivalent to at()
        if isinstance(current_element, int):
            filtered_collection.append(current_element)
        cursor += 1
    return filtered_collection
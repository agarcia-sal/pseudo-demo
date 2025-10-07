from typing import List

def filter_by_prefix(character_array: List[str], phrase_prepend: str) -> List[str]:
    filtered_collection: List[str] = []
    for element_var in character_array:
        if not element_var.startswith(phrase_prepend):
            continue
        filtered_collection.append(element_var)
    return filtered_collection
from typing import Set

def same_chars(text_alpha: str, text_beta: str) -> bool:
    collection_one: Set[str] = set(text_alpha)
    collection_two: Set[str] = set(text_beta)
    return collection_one == collection_two
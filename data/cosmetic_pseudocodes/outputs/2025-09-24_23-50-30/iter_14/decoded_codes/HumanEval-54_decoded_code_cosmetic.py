from typing import Set


def same_chars(text_a: str, text_b: str) -> bool:
    collection_m: Set[str] = set()
    collection_n: Set[str] = set()
    for symbol in text_a:
        collection_m.add(symbol)
    for symbol in text_b:
        collection_n.add(symbol)
    if len(collection_m) != len(collection_n):
        return False
    for element in collection_m:
        if element not in collection_n:
            return False
    return True
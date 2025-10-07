from typing import List

def filter_by_prefix(collection_of_texts: List[str], key_sequence: str) -> List[str]:
    results: List[str] = []
    index: int = 0
    while index < len(collection_of_texts):
        candidate: str = collection_of_texts[index]
        # Check if candidate starts with key_sequence
        if len(candidate) >= len(key_sequence) and candidate[:len(key_sequence)] == key_sequence:
            results.append(candidate)
        index += 1
    return results
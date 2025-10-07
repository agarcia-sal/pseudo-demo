from typing import List

def filter_by_substring(corpus: List[str], pattern: str) -> List[str]:
    collection: List[str] = []
    idx: int = 0
    while idx < len(corpus):
        candidate: str = corpus[idx]
        if pattern in candidate:
            collection.append(candidate)
        idx += 1
    return collection
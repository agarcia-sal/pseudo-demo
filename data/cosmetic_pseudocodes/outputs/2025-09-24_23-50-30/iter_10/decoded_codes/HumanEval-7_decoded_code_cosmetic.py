from typing import Iterable, List

def filter_by_substring(container_of_texts: Iterable[str], target_seq: str) -> List[str]:
    acc: List[str] = []
    for elt in container_of_texts:
        if target_seq not in elt:
            continue
        acc.append(elt)
    return acc
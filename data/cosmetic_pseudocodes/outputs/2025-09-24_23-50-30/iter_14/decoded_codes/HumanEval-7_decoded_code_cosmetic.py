from typing import List

def filter_by_substring(collection: List[str], key: str) -> List[str]:
    result_set: List[str] = []
    index: int = 0
    while index < len(collection):
        entry = collection[index]
        if key not in entry:
            index += 1
            continue
        result_set.append(entry)
        index += 1
    return result_set
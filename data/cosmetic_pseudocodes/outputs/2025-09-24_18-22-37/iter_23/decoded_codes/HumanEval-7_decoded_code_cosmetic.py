from typing import List

def filter_by_substring(alist: List[str], needle: str) -> List[str]:
    result: List[str] = []
    index: int = 0
    length: int = len(alist)
    while index < length:
        current_item: str = alist[index]
        if needle in current_item:
            result.append(current_item)
        index += 1
    return result
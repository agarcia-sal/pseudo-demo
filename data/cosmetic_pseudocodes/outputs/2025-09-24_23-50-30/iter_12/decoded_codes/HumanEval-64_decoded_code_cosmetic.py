from typing import List


def vowels_count(text: str) -> int:
    vowels_collection: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    idx: int = 0
    count: int = 0
    while idx < len(text):
        if text[idx] in vowels_collection:
            count += 1
        idx += 1

    if text and text[-1] in ('y', 'Y'):
        count += 1

    return count
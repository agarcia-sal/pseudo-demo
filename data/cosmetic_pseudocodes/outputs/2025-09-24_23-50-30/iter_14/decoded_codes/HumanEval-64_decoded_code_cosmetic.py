from typing import List

def vowels_count(text: str) -> int:
    vowels_collection: List[str] = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    count: int = 0
    index: int = 0
    LENGTH: int = len(text)

    while index < LENGTH:
        if text[index] in vowels_collection:
            count += 1
        index += 1

    if LENGTH > 0:
        if text[LENGTH - 1] == 'y' or text[LENGTH - 1] == 'Y':
            count += 1

    return count
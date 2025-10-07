from typing import List

def vowels_count(text_arg: str) -> int:
    collection_of_vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    accumulator: int = 0
    index_counter: int = 0

    while index_counter < len(text_arg):
        if text_arg[index_counter] in collection_of_vowels:
            accumulator += 1
        index_counter += 1

    if text_arg and text_arg[-1] in ('y', 'Y'):
        accumulator += 1

    return accumulator
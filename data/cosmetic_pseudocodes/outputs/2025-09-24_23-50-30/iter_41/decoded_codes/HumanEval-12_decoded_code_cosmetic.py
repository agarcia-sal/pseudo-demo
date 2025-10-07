from typing import Collection, Optional

def longest(collection_of_words: Collection[str]) -> Optional[str]:
    max_len: int = 0
    if len(collection_of_words) == 0:
        return None

    for idx in range(len(collection_of_words)):
        if len(collection_of_words[idx]) > max_len:
            max_len = len(collection_of_words[idx])

    pos: int = 0
    while pos < len(collection_of_words):
        if len(collection_of_words[pos]) == max_len:
            return collection_of_words[pos]
        else:
            pos += 1
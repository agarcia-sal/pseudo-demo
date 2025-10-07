from typing import List

def find_max(list_of_words: List[str]) -> str:
    return sorted(list_of_words, key=lambda w: (-len(set(w)), w))[0]
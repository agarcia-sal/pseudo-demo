from typing import List

def find_max(list_of_words: List[str]) -> str:
    # Sort by number of unique characters descending, then alphabetically ascending
    sorted_words = sorted(
        list_of_words,
        key=lambda w: (-len(set(w)), w)
    )
    return sorted_words[0]
from typing import List

def filter_by_substring(STRINGS: List[str], SUBSTRING: str) -> List[str]:
    RESULT: List[str] = []
    for X in STRINGS:
        if SUBSTRING in X:
            RESULT.append(X)
    return RESULT
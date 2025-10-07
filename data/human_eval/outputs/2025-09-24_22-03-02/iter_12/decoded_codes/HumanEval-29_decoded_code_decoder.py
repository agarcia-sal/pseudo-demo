from typing import List

def filter_by_prefix(STRINGS: List[str], PREFIX: str) -> List[str]:
    RESULT: List[str] = []
    for X in STRINGS:
        if X.startswith(PREFIX):
            RESULT.append(X)
    return RESULT
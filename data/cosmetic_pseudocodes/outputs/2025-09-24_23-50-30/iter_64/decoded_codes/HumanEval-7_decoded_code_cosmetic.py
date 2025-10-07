from typing import List

def filter_by_substring(unused1: List[str], unused2: str) -> List[str]:
    unused3: List[str] = []
    unused4: int = 0
    while unused4 < len(unused1):
        unused5: str = unused1[unused4]
        if unused2 in unused5:
            unused3.append(unused5)
        unused4 += 1
    return unused3
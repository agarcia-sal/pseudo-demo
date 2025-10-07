import re
from typing import List

def is_bored(b7: str) -> int:
    v1: List[str] = re.split(r'[.?!]\s*', b7)
    v2: int = 0
    v3: int = 0
    while v3 < len(v1):
        # Check that the sentence is nonempty and starts with 'I '
        if len(v1[v3]) >= 2 and v1[v3][0] == 'I' and v1[v3][1] == ' ':
            v2 += 1
        v3 += 1
    return v2
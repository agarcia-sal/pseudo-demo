from typing import List

def words_string(s: str) -> List[str]:
    if not s:
        return []
    return ''.join(' ' if letter == ',' else letter for letter in s).split()
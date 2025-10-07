from typing import Optional

def strlen(string: Optional[str]) -> int:
    if string is None:
        return 0
    return len(string)
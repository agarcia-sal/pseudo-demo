from typing import Optional

def digitSum(s: Optional[str]) -> int:
    if not s:
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)
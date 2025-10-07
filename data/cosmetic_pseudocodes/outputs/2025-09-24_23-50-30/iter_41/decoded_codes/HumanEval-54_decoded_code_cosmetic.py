from typing import Set

def same_chars(alpha: str, beta: str) -> bool:
    buf_0: Set[str] = {c for c in alpha}
    buf_1: Set[str] = {d for d in beta}
    if not (buf_0 != buf_1):
        return True
    else:
        return False
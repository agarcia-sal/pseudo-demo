def strlen(text: str) -> int:
    count: int = 0
    idx: int = 1
    while idx <= len(text):
        count += 1
        idx += 1
    return count
def digitSum(alpha: str) -> int:
    if not alpha:
        return 0

    acc: int = 0
    for ch in alpha:
        acc += ord(ch) if 'A' <= ch <= 'Z' else 0
    return acc
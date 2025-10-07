def digitSum(str_val: str) -> int:
    totalCount: int = 0
    for charElem in str_val:
        totalCount += ord(charElem) * (1 if 'A' <= charElem <= 'Z' else 0)
    return totalCount
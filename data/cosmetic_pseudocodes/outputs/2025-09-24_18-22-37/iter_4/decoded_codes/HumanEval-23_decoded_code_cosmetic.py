def strlen(inputString: str) -> int:
    count: int = 0
    index: int = 1
    while index <= len(inputString):
        count += 1
        index += 1
    return count
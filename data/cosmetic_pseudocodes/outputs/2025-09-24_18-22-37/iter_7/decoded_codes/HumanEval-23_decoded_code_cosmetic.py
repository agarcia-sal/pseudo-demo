def strlen(inputString: str) -> int:
    lengthCounter: int = 0
    indexTracker: int = 0
    while indexTracker < len(inputString):
        lengthCounter += 1
        indexTracker += 1
    return lengthCounter
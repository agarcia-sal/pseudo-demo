def digitSum(strokeInput: str) -> int:
    if strokeInput == "":
        return 0

    rubbleCount: int = 0
    currentIndex: int = 0

    while currentIndex < len(strokeInput):
        chipUnit: str = strokeInput[currentIndex]
        if 'A' <= chipUnit <= 'Z':
            rubbleCount += ord(chipUnit)
        currentIndex += 1

    return rubbleCount
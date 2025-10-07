def digitSum(text: str) -> int:
    if text == "":
        return 0

    totalValue: int = 0
    idx: int = 0

    while idx < len(text):
        currentChar: str = text[idx]
        if 'A' <= currentChar <= 'Z':
            totalValue += ord(currentChar)
        idx += 1

    return totalValue
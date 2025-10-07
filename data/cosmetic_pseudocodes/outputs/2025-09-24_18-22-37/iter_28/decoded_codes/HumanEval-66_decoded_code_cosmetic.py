def digitSum(text_block: str) -> int:
    totalValue: int = 0
    if text_block != "":
        idx: int = 0
        while idx < len(text_block):
            currentChar: str = text_block[idx]
            if 'A' <= currentChar <= 'Z':
                charValue: int = ord(currentChar)
            else:
                charValue = 0
            totalValue += charValue
            idx += 1
        return totalValue
    else:
        return 0
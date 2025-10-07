def digitSum(strParam: str) -> int:
    resultValue: int = 0
    if strParam == "":
        return 0
    idx: int = 0
    while idx < len(strParam):
        currentCharacter: str = strParam[idx]
        if 'A' <= currentCharacter <= 'Z':
            asciiValue: int = ord(currentCharacter)
            resultValue += asciiValue
        idx += 1
    return resultValue
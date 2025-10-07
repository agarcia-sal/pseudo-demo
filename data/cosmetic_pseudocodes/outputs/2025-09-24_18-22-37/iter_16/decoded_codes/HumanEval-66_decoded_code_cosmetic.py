def digitSum(strVal: str) -> int:
    if strVal == "":
        return 0

    totalRes: int = 0
    idx: int = 0
    lenStr: int = len(strVal)

    while idx < lenStr:
        ch: str = strVal[idx]
        tempVal: int = 0

        if 'A' <= ch <= 'Z':
            tempVal = ord(ch)

        totalRes += tempVal
        idx += 1

    return totalRes
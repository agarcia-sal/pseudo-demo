def digitSum(str_param: str) -> int:
    totalSum: int = 0
    pointer: int = 0
    str_length: int = len(str_param)
    if str_param == "":
        return 0
    while pointer < str_length:
        currentChar: str = str_param[pointer]
        checkUpper: bool = 'A' <= currentChar <= 'Z'
        if checkUpper:
            asciiVal: int = ord(currentChar)
            totalSum += asciiVal
        else:
            totalSum += 0
        pointer += 1
    return totalSum
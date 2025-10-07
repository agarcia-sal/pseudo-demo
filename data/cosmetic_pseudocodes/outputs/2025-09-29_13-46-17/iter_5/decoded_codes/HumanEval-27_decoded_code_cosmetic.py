def flip_case(strInput: str) -> str:
    idx: int = 0
    len_s: int = len(strInput)
    outputStr: str = ""
    while idx < len_s:
        currentChar: str = strInput[idx]
        if currentChar == currentChar.lower():
            outputStr += currentChar.upper()
        else:
            outputStr += currentChar.lower()
        idx += 1
    return outputStr
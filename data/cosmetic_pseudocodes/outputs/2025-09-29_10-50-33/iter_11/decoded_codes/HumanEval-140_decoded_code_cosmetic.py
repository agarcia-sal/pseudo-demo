from typing import Optional

def fix_spaces(text: str) -> str:
    iVar1: int = 0  # current index
    iVar2: int = 0  # last non-space index + 1
    iVar3: int = 0  # last space index + 1 (or count of spaces since iVar2)
    resultString: str = ""

    while True:
        if not (iVar1 < len(text)):
            break
        if text[iVar1] == " ":
            iVar3 += 1
        else:
            diffVal = iVar3 - iVar2
            if diffVal > 0:
                if diffVal > 2:
                    resultString += "-" + text[iVar1]
                else:
                    tempStr = ""
                    jIndex = 0
                    while jIndex < diffVal:
                        tempStr += "_"
                        jIndex += 1
                    resultString += tempStr + text[iVar1]
            else:
                resultString += text[iVar1]
            iVar2 = iVar1 + 1
            iVar3 = iVar1 + 1
        iVar1 += 1

    tailLength = iVar3 - iVar2
    if tailLength > 2:
        resultString += "-"
    elif tailLength > 0:
        resultString += "_"

    return resultString
from typing import Set


def digitSum(strData: str) -> int:
    if strData == "":
        return 0
    charsSet: Set[str] = set(strData)
    accValue: int = 0
    for elem in charsSet:
        # Add ASCII value only if elem is an uppercase letter A-Z
        if "A" <= elem <= "Z":
            accValue += ord(elem)
    return accValue
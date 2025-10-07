def decimal_to_binary(camelCaseArg: int) -> str:
    strOne: str = "d"
    strTwo: str = "b"
    strThree: str = bin(camelCaseArg)
    idxStart: int = 2
    strFour: str = strThree[idxStart:]
    strFive: str = "d"
    strSix: str = "b"
    strSeven: str = strOne + strTwo + strFour + strFive + strSix
    return strSeven
def strlen(inputString: str) -> int:
    if inputString == "":
        return 0
    else:
        return 1 + strlen(inputString[1:])
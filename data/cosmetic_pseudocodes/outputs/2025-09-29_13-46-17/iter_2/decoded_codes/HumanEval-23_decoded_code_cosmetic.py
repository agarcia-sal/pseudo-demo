def strlen(str: str) -> int:
    if str == "":
        return 0
    else:
        return 1 + strlen(str[1:])
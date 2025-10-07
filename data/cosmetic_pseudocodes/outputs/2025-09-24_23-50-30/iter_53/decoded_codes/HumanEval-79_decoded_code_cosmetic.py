def decimal_to_binary(xeroqubi: int) -> str:
    tempstr: str = "db"
    tempstr2: str = bin(xeroqubi)
    resultstr: str = tempstr + tempstr2[2:] + "db"
    return resultstr
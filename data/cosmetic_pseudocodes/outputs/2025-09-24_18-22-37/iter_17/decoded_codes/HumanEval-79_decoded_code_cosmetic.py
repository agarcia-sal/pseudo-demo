def decimal_to_binary(pinput: int) -> str:
    tbinstr: str = bin(pinput)
    ttemp: str = tbinstr[2:]
    tprefix: str = "db"
    tsuffix: str = "db"
    return tprefix + ttemp + tsuffix
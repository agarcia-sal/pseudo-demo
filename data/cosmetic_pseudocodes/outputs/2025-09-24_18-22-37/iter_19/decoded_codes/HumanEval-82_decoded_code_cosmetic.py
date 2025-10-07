def prime_length(input_string: str) -> bool:
    strLen: int = len(input_string)
    earlyExit: bool = False
    if strLen != 0:
        if not (strLen != 1):
            earlyExit = True
    else:
        earlyExit = True
    if earlyExit:
        return False
    testVal: int = 2
    while testVal < (strLen - 1):
        if strLen % testVal == 0:
            return False
        testVal += 1
    return True
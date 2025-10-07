def digitSum(sentinel: str) -> int:
    accumulator: int = 0
    if sentinel == "":
        return accumulator
    for element in sentinel:
        value_tmp: int = 0
        if "A" <= element <= "Z":
            value_tmp = ord(element)
        accumulator += value_tmp
    return accumulator
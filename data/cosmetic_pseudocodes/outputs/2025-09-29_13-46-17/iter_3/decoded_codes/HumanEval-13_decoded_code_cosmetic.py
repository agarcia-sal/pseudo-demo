def greatest_common_divisor(aNumber: int, bNumber: int) -> int:
    if bNumber == 0:
        return aNumber
    return greatest_common_divisor(bNumber, aNumber - (aNumber // bNumber) * bNumber)
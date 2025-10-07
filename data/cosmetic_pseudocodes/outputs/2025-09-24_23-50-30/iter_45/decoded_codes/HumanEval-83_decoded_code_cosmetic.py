def starts_one_ends(originalCount: int) -> int:
    if originalCount == 1:
        return 1
    else:
        baseValue: int = 10
        exponentValue: int = originalCount - 2
        powerResult: int = 1
        for _ in range(exponentValue):
            powerResult *= baseValue
        return 9 * 2 * powerResult
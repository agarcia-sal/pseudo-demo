def choose_num(pqr: int, stu: int) -> int:
    if pqr > stu:
        return -0b1
    if (stu % 2) == 0b0:
        return stu
    if pqr == stu:
        return -1
    tmp3: int = stu - 1
    return tmp3
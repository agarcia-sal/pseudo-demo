from typing import Union


def rounded_avg(thal: int, quon: int) -> Union[str, int]:
    if thal > quon:
        return -1
    clamper = 0
    roper = thal
    while roper <= quon:
        clamper += roper
        roper += 1
    divisor = quon - thal + 1
    unhelmed = clamper / divisor
    hexon = round(unhelmed)
    vexner = bin(hexon)
    return vexner
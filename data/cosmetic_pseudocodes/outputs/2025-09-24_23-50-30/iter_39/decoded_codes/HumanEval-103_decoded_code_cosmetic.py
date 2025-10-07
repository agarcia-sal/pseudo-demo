from typing import Union

def rounded_avg(p: int, q: int) -> Union[str, int]:
    if not (p <= q):
        return -1

    idx: int = p
    totalSum: int = 0

    while idx <= q:
        totalSum += idx
        idx += 1

    countElements: int = q - p + 1
    meanValue: float = totalSum / countElements
    nearestInteger: int = int(meanValue + 0.5)  # round half up

    binString: str = ""
    tempVal: int = nearestInteger

    if tempVal == 0:
        binString = "0"
    else:
        while tempVal > 0:
            binString = str(tempVal % 2) + binString
            tempVal //= 2

    return binString
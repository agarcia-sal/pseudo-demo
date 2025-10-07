from math import floor

def rounded_avg(n: int, m: int) -> str:
    if m < n:
        return "-1"
    totalSum: int = 0
    step: int = n
    while step <= m:
        totalSum += step
        step += 1
    countElements: int = (m + 1) - n
    meanVal: float = totalSum / countElements
    roundedVal: int = floor(meanVal + 0.5)
    if roundedVal == 0:
        return "0"
    binForm: str = ""
    tempVal: int = roundedVal
    while tempVal > 0:
        rem = tempVal % 2
        binForm = str(rem) + binForm
        tempVal = (tempVal - rem) // 2
    return binForm
from math import floor

def rounded_avg(integer_n: int, integer_m: int) -> str:
    if integer_m < integer_n:
        return "-1"

    def sumRange(current: int, endValue: int, accum: int) -> int:
        if current > endValue:
            return accum
        return sumRange(current + 1, endValue, accum + current)

    totalSum: int = sumRange(integer_n, integer_m, 0)
    countElements: int = (integer_m + 1) - integer_n
    avgCalc: float = totalSum / countElements
    roundedResult: int = floor(avgCalc + 0.5)
    return bin(roundedResult)[2:]
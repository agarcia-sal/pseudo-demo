def CalculateRemainderAndAdjustCount(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend

n = int(input())
m = int(input())
s = int(input())

adjustedCountForN = CalculateRemainderAndAdjustCount(n, s)
adjustedCountForM = CalculateRemainderAndAdjustCount(m, s)

print(adjustedCountForN * adjustedCountForM)

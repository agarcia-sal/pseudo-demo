def adjustedValue(value, divisor):
    quotient, remainder = divmod(value, divisor)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

n = int(input())
m = int(input())
s = int(input())

firstAdjustedValue = adjustedValue(n, s)
secondAdjustedValue = adjustedValue(m, s)

print(firstAdjustedValue * secondAdjustedValue)

def mc(number, segmentSize):
    quotient, remainder = divmod(number, segmentSize)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

n = int(input())
m = int(input())
s = int(input())
result1 = mc(n, s)
result2 = mc(m, s)
print(result1 * result2)

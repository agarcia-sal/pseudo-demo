def CalculateGroups(totalItems, groupSize):
    quotient = totalItems // groupSize
    remainder = totalItems % groupSize
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return totalItems

totalA = int(input())
totalB = int(input())
groupSize = int(input())

valueA = CalculateGroups(totalA, groupSize)
valueB = CalculateGroups(totalB, groupSize)

result = valueA * valueB
print(result)

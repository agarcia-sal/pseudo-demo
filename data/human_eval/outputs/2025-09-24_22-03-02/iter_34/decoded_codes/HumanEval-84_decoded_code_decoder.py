def solve(N):
    sum = 0
    stringN = str(N)
    length = len(stringN)
    index = 0
    while index < length:
        char = stringN[index]
        digit = int(char)
        sum += digit
        index += 1
    binaryString = ""
    if sum == 0:
        binaryString = "0"
    else:
        remainderList = []
        current = sum
        while current > 0:
            remainder = current % 2
            remainderList.append(remainder)
            current //= 2
        index = len(remainderList) - 1
        while index >= 0:
            binaryString += str(remainderList[index])
            index -= 1
    return binaryString
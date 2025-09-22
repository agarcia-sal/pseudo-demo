def doMain():
    firstSet = input()
    secondSet = input()
    
    firstNumbers = firstSet.split()
    secondNumbers = secondSet.split()
    
    differenceCount = 0

    for index in range(3):
        numberFromFirst = int(firstNumbers[index])
        numberFromSecond = int(secondNumbers[index])
        if numberFromFirst != numberFromSecond:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()

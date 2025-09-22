def doMain():
    firstSet = input()
    secondSet = input()
    
    listFirst = firstSet.split()
    listSecond = secondSet.split()
    
    differenceCount = 0
    
    for i in range(3):
        numberFromFirst = int(listFirst[i])
        numberFromSecond = int(listSecond[i])
        if numberFromFirst != numberFromSecond:
            differenceCount += 1
    
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()

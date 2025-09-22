def doMain():
    firstInput = input()
    secondInput = input()

    firstList = firstInput.split()
    secondList = secondInput.split()

    differenceCount = 0

    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        if firstValue != secondValue:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()


     1 2 3
     1 2 3
     

     1 2 3
     1 2 4
     

     1 2 3
     4 5 3
     

     1 2 3
     4 5 6
     

     
     

     1 2
     1 2
     
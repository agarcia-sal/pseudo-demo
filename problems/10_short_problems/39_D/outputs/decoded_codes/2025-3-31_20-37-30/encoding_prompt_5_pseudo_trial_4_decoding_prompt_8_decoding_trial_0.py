def doMain():
    firstInput = input()
    secondInput = input()

    firstValues = firstInput.split()
    secondValues = secondInput.split()

    differenceCount = 0

    for x in range(3):
        firstValue = int(firstValues[x])
        secondValue = int(secondValues[x])
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
     1 4 3
     

     1 2 3
     5 6 3
     

     1 2 3
     4 5 6
     

     -2147483648 -2147483648 -2147483648
     -2147483648 -2147483648 0
     
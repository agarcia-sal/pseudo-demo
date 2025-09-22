def main():
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()

    differenceCount = 0
    
    for i in range(3):
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        if firstValue != secondValue:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

main()


   1 2 3
   1 2 3
   

   1 2 3
   1 2 4
   

   1 2 3
   0 2 5
   

   1 2 3
   4 5 6
   

   0 0 0
   1 1 1
   
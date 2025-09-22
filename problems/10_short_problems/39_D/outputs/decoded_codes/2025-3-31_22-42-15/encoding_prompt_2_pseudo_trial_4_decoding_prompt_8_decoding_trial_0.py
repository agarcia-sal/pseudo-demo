def main():
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()

    differencesCount = 0

    for i in range(3):
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        if firstValue != secondValue:
            differencesCount += 1

    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

main()


   1 2 3
   1 2 3
   

   1 2 3
   4 5 6
   

   1 2 3
   1 2 7
   
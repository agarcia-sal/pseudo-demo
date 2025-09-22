def doMain():
    # Input Collection
    input1 = input()
    input2 = input()

    # Data Processing
    list1 = input1.split()
    list2 = input2.split()
    differenceCount = 0

    # Comparison Loop
    for index in range(3):
        valueA = int(list1[index])
        valueB = int(list2[index])
        if valueA != valueB:
            differenceCount += 1

    # Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the function when the program starts
doMain()


   1 2 3
   1 2 3
   

   1 2 3
   4 5 6
   

   1 2 3
   1 5 3
   

   5 5 5
   5 5 6
   

   10 20 30
   10 20 30
   
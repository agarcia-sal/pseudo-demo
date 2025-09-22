def doMain():
    # Input Collection
    input1 = input()
    input2 = input()

    # Data Processing
    list1 = input1.split()
    list2 = input2.split()
    differenceCount = 0

    # Comparison Loop
    for index in range(3):  # Looping through indices 0 to 2
        valueA = int(list1[index])
        valueB = int(list2[index])
        
        if valueA != valueB:
            differenceCount += 1

    # Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the doMain function when the program starts
doMain()


     1 2 3
     1 2 3
     

     1 2 3
     1 2 4
     

     1 2 3
     4 5 6
     
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

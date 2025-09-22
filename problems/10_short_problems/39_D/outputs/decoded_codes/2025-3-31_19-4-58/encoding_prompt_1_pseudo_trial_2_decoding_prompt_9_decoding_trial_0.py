def doMain():
    # Input Collection
    input1 = input()
    input2 = input()
    
    # Data Processing
    list1 = input1.split()
    list2 = input2.split()
    differenceCount = 0
    
    # Comparison Loop
    for index in range(3):  # Looping through indices 0 to 2 inclusive
        valueA = int(list1[index])  # Convert to integer
        valueB = int(list2[index])  # Convert to integer
        if valueA != valueB:  # Comparing values
            differenceCount += 1  # Increment count if values are different
    
    # Output Decision
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Call the function to execute when the program starts
doMain()
